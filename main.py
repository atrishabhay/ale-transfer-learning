import cv2
from ob_detection.template_matching import *
from environments.mario import *
import time

def match_template_test():
    tm = TemplateMatching()
    res_img = tm.match_templates()
    tm.save_img(res_img)

def test_env():
    game = Mario()

    for i in range(100):
        print(i)
        print(game.perform_move(game._env.action_space.sample()))

def main():
    game = Mario()
    tm = TemplateMatching()
    it = 0
    for i in range(300):
        move = game._env.action_space.sample()#int(input())
        #if move==-1:
        #    break
        frame = game.perform_move(move)
        res_img = tm.match_templates(frame, compress=False)
        if 200<i<300:
            tm.save_img(res_img, file_name='res_'+str(it))
            #tm.save_img(frame, file_name='frame_'+str(it))
            it+=1

if __name__=='__main__':
    #match_template_test()
    start = time.time()
    main()#test_env()
    print(time.time()-start)
