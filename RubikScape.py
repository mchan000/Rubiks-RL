from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
import random

import Rubik
from Rubik import *

class RubiksEnv(Env):
    def move(self, action):
        """Moves the cube given discrete value"""
        if action == 0:
            self.state.u()
            # print('u')
        elif action == 1:
            self.state.up()
            # print('up')
        elif action == 2:
            self.state.d()
            # print('d')
        elif action == 3:
            self.state.dp()
            # print('dp')
        elif action == 4:
            self.state.l()
            # print('l')
        elif action == 5:
            self.state.lp()
            # print('lp')
        elif action == 6:
            self.state.r()
            # print('r')
        elif action == 7:
            self.state.rp()
            # print('rp')
        elif action == 8:
            self.state.f()
            # print('f')
        elif action == 9:
            self.state.fp()
            # print('fp')
        elif action == 10:
            self.state.b()
            # print('b')
        elif action == 11:
            self.state.bp()
            # print('bp')

    def __init__(self):
        # Actions: u, u', d, d', l, l', r, r', f, f', b, b'
        self.action_space = Discrete(12)
        # 3D array
        self.observation_space = Box(low=0, high=5, shape=(6, 3, 3), dtype=int)

        self.state = Rubik.Cube()
        self.state.shuffle()

        self.moves = 100



    def step(self, action):
        self.move(action)
        self.moves -= 1

        solvedCube = Rubik.Cube()

        reward = Rubik.compare(solvedCube, self.state)

        if reward == 54:
            print('Solved!')

        if self.moves <= 0:
            done = True
        else:
            done = False

        info = {}

        return self.state, reward, done, info

    def render(self):
        pass
        # print(self.state)

    def reset(self):
        self.state = Rubik.Cube()
        self.state.shuffle()

        self.moves = 100

        return self.state

if __name__ == '__main__':
    env = RubiksEnv()

    episodes = 10
    for episode in range(1, episodes + 1):
        state = env.reset()
        done = False
        score = 0

        while not done:
            env.render()
            action = env.action_space.sample()
            n_state, reward, done, info = env.step(action)
            score = reward
        print ('Episode:{} Score:{}'.format(episode, score))
