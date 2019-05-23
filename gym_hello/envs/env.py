#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Minimal example OpenAI Gym environment.
"""
# 3rd party modules
from gym import spaces
import gym
import numpy as np

TOTAL_TIME_STEPS = 3

class HelloEnv(gym.Env):
    """
    A minimal environment with fixed episode length, two actions and fixed reward
    """


    def __init__(self):
        self.__version__ = "0.1.0"

        # General variables defining the environment
        self.current_step = -1
        self.is_done = False

        # Define what the agent can do, i.e. two discrete actions
        self.action_space = spaces.Discrete(2)

        # Observation is the remaining time
        low = np.array([0.0])
        high = np.array([TOTAL_TIME_STEPS])
        self.observation_space = spaces.Box(low, high, dtype=np.float32)


    def step(self, action):
        """
        The agent takes a step in the environment.

        Parameters
        ----------
        action : int

        Returns
        -------
        ob, reward, episode_over, info : tuple
            ob (object) :
                an environment-specific object representing your observation of
                the environment.
            reward (float) :
                amount of reward achieved by the previous action. The scale
                varies between environments, but the goal is always to increase
                your total reward.
            episode_over (bool) :
                whether it's time to reset the environment again. Most (but not
                all) tasks are divided up into well-defined episodes, and done
                being True indicates the episode has terminated. (For example,
                perhaps the pole tipped too far, or you lost your last life.)
            info (dict) :
                 diagnostic information useful for debugging. It can sometimes
                 be useful for learning (for example, it might contain the raw
                 probabilities behind the environment's last state change).
                 However, official evaluations of your agent are not allowed to
                 use this for learning.
        """
        if not self.action_space.contains(action):
            raise RuntimeError('Invalid action: {}'.format(action))

        if self.is_done:
            raise RuntimeError("Episode is done")

        self.current_step += 1
        self.is_done = self.current_step >= TOTAL_TIME_STEPS

        reward = 100.0 if self.is_done else -1
        state = self._get_state()
        return state, reward, self.is_done, {}

    def _get_state(self):
        return [TOTAL_TIME_STEPS - self.current_step]

    def reset(self):
        """
        Reset the state of the environment and returns an initial observation.

        Returns
        -------
        observation (object): the initial observation of the space.
        """
        self.current_step = 0
        self.is_done = False
        return self._get_state()

    def render(self, mode='human', close=False):
        return '╭∩╮(Ο_Ο)╭∩╮'

    def seed(self, seed):
        pass
