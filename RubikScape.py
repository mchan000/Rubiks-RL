from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
import random
from stable_baselines3.common.env_checker import check_env
from stable_baselines3 import PPO

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
        self.done = False
        self.moves_made = 0
        self.state = Rubik.Cube()
        self.state.shuffle()

        self.previous_moves = []
        self.previous_state = []
        self.reward = 0

        self.observation = [self.previous_moves]
        self.observation = np.array(self.observation)
        self.action_space = Discrete(12)

        self.observation_space = Box(low=0, high=5, shape=(54, ), dtype=int)

    def step(self, action):

        self.move(action)
        self.moves_made += 1
        self.previous_moves.append(action)
        np.append(self.previous_state,(flattenCube(self.state)))

        solved_cube = Rubik.Cube()

        if compare(self.state, solved_cube) == 54:
            self.reward = 1
            self.done = True
        elif self.moves_made >= 100:
            self.done = True
            self.reward = compare(self.state, solved_cube)
            self.reward = 0
        else:
            self.reward = 0

        np.append(self.observation, self.state)
        info = {1: self.moves_made}
        return self.observation, self.reward, self.done, info

    def reset(self):
        # Initial scrambled cube state, moves allowed, and pevious move
        self.done = False
        self.moves_made = 0
        self.state = Rubik.Cube()
        self.state.shuffle()

        self.previous_moves = [0]
        self.previous_state = flattenCube(self.state)
        self.reward = 0
        # set observation to array of current cube state
        self.observation = np.array(flattenCube(self.state))

        return self.observation

    def render(self):
        print(self.state)


if __name__ == '__main__':
    env = RubiksEnv()

    # print(env.observation_space.sample())
    # print(env.step(1))
    # print(env.step(10))
    # print(env.reset())
    # check_env(env)

    episodes = 100

    PPO_Path = os.path.join('training', 'saved models', 'PPO_5_1R')
    model = PPO.load(PPO_Path, env=env)

    count = 0
    for episode in range(1, episodes+1):
        obs = env.reset()
        done = False
        score = 0

        while not done:
            action, _ = model.predict(obs)
            obs, reward, done, info = env.step(action)
            score += reward
        if score == 1:
            count += 1
        print('Episode:{} Score:{} Moves Made:{}'.format(episode, score, info.get(1)))

    print(count/episodes)
