from ob_detection.template_matching import *

def match_template_test():
    tm = TemplateMatching()
    res_img = tm.match_templates('test')
    tm.process_results(res_img)

if __name__=='__main__':
    match_template_test()
