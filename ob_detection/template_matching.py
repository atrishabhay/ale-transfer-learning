import cv2
from ob_detection.config import *
import numpy as np
from matplotlib import pyplot as plt
import os

class TemplateMatching:
    def __init__(self, *args, **kwargs):
        '''
        Load templates which will be used for multiple frames.
        Templates defined in config file
        '''
        self.templates = dict()
        self.template_dims = dict()
        self.config = Config()
        self.load_templates()

    def load_templates(self):
        for name, loc in self.config.get_templates().items():
            img = cv2.imread(loc, 0) #0:Grayscale, 1:RGB without trasparency, -1:without alpha channel

            if img is not None:
                self.templates[name] = img 

        self.template_dims = {name: template.shape[::-1] for name, template in self.templates.items()}

    def match_templates(self, frame=None, compress=True):
        '''
        frame : numpy array
        compress :  True  -> Bounding boxes around the detected objects, on a copy of the frame
                    False -> Filled bounding boxes at the location of the detected objects, on a black cancas
        '''

        img_rgb = cv2.imread('ob_detection/images/frame.png') if frame is None else frame

        #Dont modify frame inplace
        img_rgb = img_rgb.copy() 
        img_final = img_rgb.copy() 

        #Fill the rectangles for matching templates. +ve: Dont Fill, -ve: Fill
        fill = 1 
        
        #Compress will create colored rectangles for each matching template on a black canvas.
        if compress:
            fill = cv2.FILLED
            img_final *= 0 #Black canvas for the final compressed frame
        
        #Input frame to rgb for template matching
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        colors = self.config.get_colors()

        for name, template in self.templates.items():
            res = cv2.matchTemplate(img_gray, template, self.config.get_method())
            threshold = 0.7#TODO Move to config
            loc = np.where(res >= threshold)

            w,h = self.template_dims[name]
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_final, pt, (pt[0] + w, pt[1] + h), colors[name], fill)

        return img_final

    def save_img(self, img, file_name='res'):
        cv2.imwrite(f'ob_detection/images/{file_name}.png',img)
