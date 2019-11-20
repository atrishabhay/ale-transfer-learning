import cv2
from ob_detection.template_matching import *
from environments.mario import *
from environments.contra import *
import matplotlib.pyplot as plt
import time

def match_template_test():
    tm = TemplateMatching()
    res_img = tm.match_templates()
    tm.save_img(res_img)

def test_env(env):
    game = env()

    for i in range(100):
        print(i)
        print(game.perform_move(game._env.action_space.sample()))

def main():
    game = Mario()
    print(game._env.action_space)
    tm = TemplateMatching()
    it = 0
    
    size = (256, 480)
    out = cv2.VideoWriter('mario.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, size)
    
    for i in range(100000):
        #move = game._env.action_space.sample()#int(input())
        move = input().strip()

        if move=='-1':
            break
        
        if move.isdigit():
            move = int(move)
            if move==9:
                tm.save_img(frame, file_name='frame_'+str(it))
                it+=1
                continue
        else:
            move=3

        frame = game.perform_move(move)
        res_img = tm.match_templates(frame, compress=False)

        cv2.imshow("img", res_img)

        frame = np.concatenate((frame, res_img), axis=0)
        out.write(frame)

        #if 1<i<300:
        #tm.save_img(res, file_name='res_'+str(it))
        #tm.save_img(frame, file_name='frame_'+str(it))
        #it+=1

    out.release()

if __name__=='__main__':
    #match_template_test()
    start = time.time()
    #main()#test_env()
    #test_env(Contra)
    main()
    print(time.time()-start)
