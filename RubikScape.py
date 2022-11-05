from gym import Env
from gym.spaces import Discrete, Box
import numpy as np

import Rubik
from Rubik import *

solved_cube = Rubik.Cube()


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
        self.done = False
        self.moves_made = 0
        self.state = Rubik.Cube()
        #self.state.shuffle()
        self.moves = []
        self.reward = 0
        self.observation = np.array(flattenCube(self.state))
        # Action space is 12 possible moves
        self.action_space = Discrete(12)
        self.observation_space = Box(low=0, high=5, shape=(54,), dtype=int)

    def step(self, action):
        self.move(action)
        self.moves_made += 1
        self.moves.append(action)
        if compare(self.state, solved_cube) == 54:
            self.reward = 1
            self.done = True
        elif self.moves_made >= 100:
            self.done = True
            self.reward = -1
        else:
            self.reward = 0

        self.observation = np.array(flattenCube(self.state))
        info = {1: self.moves, 2: self.moves_made}
        return self.observation, self.reward, self.done, info

    def reset(self):
        self.done = False
        self.moves_made = 0
        self.state = Rubik.Cube()
        #self.state.shuffle()
        self.moves = []
        self.reward = 0

        # Observation state is current shuffled rubik's cube state
        self.observation = np.array(flattenCube(self.state))
        return self.observation

    def scramble(self, seq):
        for i in seq:
            self.move(i)
        self.observation = np.array(flattenCube(self.state))
        return self.observation

    def render(self):
        print(self.state)


def convertToRNotation(arr):
    notation = ""
    for i in arr:
        if i == 0:
            notation += 'u '
        elif i == 1:
            # print('up')
            notation += 'up '
        elif i == 2:
            # print('d')
            notation += 'd '
        elif i == 3:
            # print('dp')
            notation += 'dp '
        elif i == 4:
            # print('l')
            notation += 'l '
        elif i == 5:
            # print('lp')
            notation += 'lp '
        elif i == 6:
            # print('r')
            notation += 'r '
        elif i == 7:
            # print('rp')
            notation += 'rp '
        elif i == 8:
            # print('f')
            notation += 'f '
        elif i == 9:
            # print('fp')
            notation += 'fp '
        elif i == 10:
            # print('b')
            notation += 'b '
        elif i == 11:
            # print('bp')
            notation += 'bp '
    return notation
