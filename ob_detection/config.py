import cv2

class Config:
    def __init__(self):
        self.threshold = 0.8 #TODO Should be set for each method. 0.8 is for CCOEFF_NORMED
        self._templates = {
            'mario' :{  'path':'ob_detection/images/templates/mario/mario/',
                        'color': (3, 255, 32),
                        'threshold': self.threshold,
                        'game':'mario'
                        },
            'enemy2':{  'path':'ob_detection/images/templates/mario/enemies/',
                        'color': (0, 0, 255),
                        'threshold': self.threshold,
                        'game':'mario'
                        },
            'obs1'  :{  'path':'ob_detection/images/templates/mario/obstacles/',
                        'color': (255, 162, 0),
                        'threshold': self.threshold,
                        'game':'mario'
                        },
            'mario_reward' :{  'path':'ob_detection/images/templates/mario/rewards/',
                        'color': (52, 225, 235),
                        'threshold': self.threshold,
                        'game':'mario'
                        },
            'contra' :{  'path':'ob_detection/images/templates/contra/contra/',
                        'color': (0, 0, 0),
                        'threshold': self.threshold,
                        'game':'contra'
                        },
            'contra_enemy':{  'path':'ob_detection/images/templates/contra/enemies/',
                        'color': (0, 0, 255),
                        'threshold': self.threshold,
                        'game':'contra'
                        },
            'contra_obs'  :{  'path':'ob_detection/images/templates/contra/obstacles/',
                        'color': (255, 162, 0),
                        'threshold': self.threshold,
                        'game':'contra'
                        }
        }

        self.methods = {
            'CCOEFF':cv2.TM_CCOEFF, 
            'CCOEFF_NORMED':cv2.TM_CCOEFF_NORMED, 
            'CCORR':cv2.TM_CCORR,
            'CCORR_NORMED':cv2.TM_CCORR_NORMED, 
            'SQDIFF':cv2.TM_SQDIFF, 
            'SQDIFF_NORMED':cv2.TM_SQDIFF_NORMED
        }

        #To be used outside the class
        self.templates = None
        self.colors = None
        self.method = self.methods['CCOEFF_NORMED']
    
    def get_templates(self):
        '''
        Return template images corresponding to all templates defined in _templates
        '''
        if self.templates:
            return self.templates

        #Initialize template images from template definitions
        self.templates = {name: template['path'] for name, template in self._templates.items()}
        return self.templates
    
    def get_colors(self):
        '''
        Return colors to be filled(for each template defined in _templates) when a template match is detected in a frame 
        '''
        if self.colors:
            return self.colors
        
        #Initialize colors from template definitions
        self.colors = {name: template['color'] for name, template in self._templates.items()}
        return self.colors
    
    def get_method(self):
        return self.method
