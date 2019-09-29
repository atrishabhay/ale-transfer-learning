from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

class Mario:
    def __init__(self, *args, **kwargs):
        self._env = gym_super_mario_bros.make(kwargs.get('env','SuperMarioBros-v0'))
        self._env = JoypadSpace(self._env, SIMPLE_MOVEMENT)
        self._env.reset()

        self._cur_state  = None
        self._cur_reward = None

    def perform_move(self, move):
        state, reward, done, info = self._env.step(move)
        self._cur_state  = state
        self._cur_reward = reward

        self._env.render()
        return self._cur_state
    
    def get_cur_reward(self):
        return self._cur_reward

    def get_cur_state(self):
        return self._cur_state
