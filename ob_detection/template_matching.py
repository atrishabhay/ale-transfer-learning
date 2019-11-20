import cv2
from ob_detection.config import *
import numpy as np
from matplotlib import pyplot as plt
import os
from collections import defaultdict

class TemplateMatching:
    def __init__(self, *args, **kwargs):
        '''
        Load templates which will be used for multiple frames.
        Templates defined in config file
        '''
        self.templates = defaultdict(dict)
        self.template_dims = dict()
        self.config = Config()
        self.load_templates()
        
        self.colors = self.config.get_colors()

    def load_templates(self):
        for obj_type, loc in self.config.get_templates().items():
            for _file in os.listdir(loc):
                name, _ = _file.split('.')
                img = cv2.imread(loc+_file, 0) #0:Grayscale, 1:RGB without trasparency, -1:without alpha channel

                if img is not None:
                    self.templates[obj_type][name] = img

        self.template_dims = {obj_type: {name: template.shape[::-1] for name, template in templates.items()} 
                                for obj_type, templates in self.templates.items()}

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

        for obj_type, templates in self.templates.items():
            for name, template in templates.items():
                res = cv2.matchTemplate(img_gray, template, self.config.get_method())
                threshold = 0.88#TODO Move to config
                loc = np.where(res >= threshold)
                w,h = self.template_dims[obj_type][name]
                if "mario" in name:
                    if "big" in name:
                        y,x = loc       
                        loc = (y-3, x-3)#Change top left corner of BB
                        w,h = 16, 31    #Size of BB
                    else:
                        y,x = loc
                        loc = (y-1, x-4)
                        w,h = 15, 15

                elif "enemy" in name:
                    if "1" in name:
                        #Mushroom top enemy
                        y,x = loc       
                        loc = (y-4, x-4)#Change top left corner of BB
                        w,h = 16, 15    #Size of BB
                    elif "2" in name:
                        y,x = loc       
                        loc = (y-10, x-4)#Change top left corner of BB
                        w,h = 16, 21    #Size of BB

                for pt in zip(*loc[::-1]):
                    cv2.rectangle(img_final, pt, (pt[0] + w, pt[1] + h), self.colors[obj_type], fill)

        return img_final

    def save_img(self, img, file_name='res'):
        cv2.imwrite(f'ob_detection/images/{file_name}.png',img)
