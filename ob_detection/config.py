import cv2

class Config:
    def __init__(self, game):
        self.threshold = 0.8 #TODO Should be set for each method. 0.8 is for CCOEFF_NORMED
        self._templates = {
            'mario_frwrd' :{  'path':'ob_detection/images/templates/mario/mario_forward.png',
                        'color': (3, 255, 32),
                        'threshold': self.threshold,
                        },
            'mario_backwrd' :{  'path':'ob_detection/images/templates/mario/mario_backward.png',
                        'color': (3, 255, 32),
                        'threshold': self.threshold,
                        },
            'enemy1':{  'path':'ob_detection/images/templates/mario/enemy1.png',
                        'color': (0, 0, 255),
                        'threshold': self.threshold,
                        },
            'obs1'  :{  'path':'ob_detection/images/templates/mario/obs1.png',
                        'color': (255, 162, 0),
                        'threshold': self.threshold,
                        },
            'obs3'  :{  'path':'ob_detection/images/templates/mario/obs3.png',
                        'color': (255, 162, 0),
                        'threshold': self.threshold,
                        },
            'obs2'  :{  'path':'ob_detection/images/templates/mario/obs2.png',
                        'color': (255, 162, 0),
                        'threshold': self.threshold,
                        },
            'brick' :{  'path':'ob_detection/images/templates/mario/brick.png',
                        'color': (255, 162, 0),
                        'threshold': self.threshold,
                        }
        }

        if game == 'sonic':
            self._templates = {
                'son1' :{  'path':'ob_detection/images/templates/sonic/son1.png',
                            'color': (3, 255, 32),
                            'threshold': self.threshold,
                            },
                'son2' :{  'path':'ob_detection/images/templates/sonic/son2.png',
                            'color': (3, 255, 32),
                            'threshold': self.threshold,
                            },
                'son3' :{  'path':'ob_detection/images/templates/sonic/son3.png',
                            'color': (3, 255, 32),
                            'threshold': self.threshold,
                            },
                'son4' :{  'path':'ob_detection/images/templates/sonic/son3.png',
                            'color': (3, 255, 32),
                            'threshold': self.threshold,
                            },
                'son5' :{  'path':'ob_detection/images/templates/sonic/son3.png',
                            'color': (3, 255, 32),
                            'threshold': self.threshold,
                            },
                'son6' :{  'path':'ob_detection/images/templates/sonic/son3.png',
                            'color': (3, 255, 32),
                            'threshold': self.threshold,
                            },
            
                'enemy1':{  'path':'ob_detection/images/templates/sonic/enemy1.png',
                            'color': (0, 0, 255),
                            'threshold': self.threshold,
                            },
                'enemy2':{  'path':'ob_detection/images/templates/sonic/enemy2.png',
                            'color': (0, 0, 255),
                            'threshold': self.threshold,
                            },
                'enemy3':{  'path':'ob_detection/images/templates/sonic/enemy3.png',
                            'color': (0, 0, 255),
                            'threshold': self.threshold,
                            },
                'enemy4':{  'path':'ob_detection/images/templates/sonic/enemy4.png',
                            'color': (0, 0, 255),
                            'threshold': self.threshold,
                            },
                'enemy5':{  'path':'ob_detection/images/templates/sonic/enemy5.png',
                            'color': (0, 0, 255),
                            'threshold': self.threshold,
                            },
                'ground1' :{  'path':'ob_detection/images/templates/sonic/ground1.png',
                            'color': (255, 162, 0),
                            'threshold': self.threshold,
                            },
                'ground2' :{  'path':'ob_detection/images/templates/sonic/ground2.png',
                            'color': (255, 162, 0),
                            'threshold': self.threshold,
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
