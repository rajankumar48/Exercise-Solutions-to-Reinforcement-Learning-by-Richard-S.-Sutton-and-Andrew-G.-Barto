# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 12:35:39 2020

@author: Rajan Kumar
"""

import numpy as np
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns

#%% Create Multi armed bandit environment

class MultiArmedBandit(object):
    def __init__(self, n_arms, mu, sigma):
        self.n_arms = n_arms
        self.mu = mu
        self.sigma = sigma
        self.Q = np.zeros(n_arms)
        self.q_star = np.zeros(n_arms)
        
    def select_action(self, epsilon):
        
        if np.random.rand() < epsilon:
            action = np.random.randint(0, self.n_arms - 1)
        else:
            action = np.random.choice(np.flatnonzero(self.Q == self.Q.max())) # random tie breaker
            # action = np.argmax(self.Q)
            
        return action
    
    def random_walk(self):
        self.q_star += np.random.normal(self.mu, self.sigma, self.n_arms)
        
    def is_optimal(self, action):
        return action == np.argmax(self.q_star)
    
    def reward(self, action):
        return np.random.normal(self.q_star[action], 1, 1)
        
class SampleAverage(MultiArmedBandit):
    def __init__(self):
        super(SampleAverage, self).__init__(n_arms, mu, sigma)
        self.arm_count = np.zeros(n_arms)
    
    def update_Q(self, action, R):
        self.arm_count[action] += 1
        self.Q[action] = self.Q[action] + (R - self.Q[action])/self.arm_count[action]
        

class WeightedAverage(MultiArmedBandit):
    def __init__(self, alpha):
        super(WeightedAverage, self).__init__(n_arms, mu, sigma)
        self.arm_count = np.zeros(n_arms)
        self.alpha = alpha
    
    def update_Q(self, action, R):
        self.Q[action] = self.Q[action] + self.alpha*(R - self.Q[action])
    
def line_plot(data, ylabel, fig_name):
    mean_data = np.mean(data, axis = 1)
    mean_data = pd.DataFrame(mean_data, columns = ['Sample Average', 'Weighted Average'])
    mean_data['Steps'] = mean_data.index + 1
    data_melt = pd.melt(mean_data, id_vars = ['Steps'], value_vars = mean_data.columns.drop('Steps'))
    fig, ax = plt.subplots(figsize = (10, 5))
    sns.lineplot(data = data_melt, x = 'Steps', y = 'value', hue = 'variable')
    ax.set_ylabel(ylabel)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles[1:], labels=labels[1:])
    fig.tight_layout()
    plt.savefig('resources/chapter 2/' + fig_name + '.png')

#%% Run the experiment

np.random.seed(123)
n_steps = 10000
n_runs = 2000
n_arms = 10
mu = 0 # center for random walk
sigma = 0.01 # standard deviation for random walk
epsilon = 0.1
alpha = 0.1 # step size

n_methods = 2

rewards = np.empty((n_steps, n_runs, n_methods))
optimals = np.empty((n_steps, n_runs, n_methods))

for run_id in tqdm(range(n_runs)):
    sample_average = SampleAverage()
    weighted_average = WeightedAverage(alpha)
    methods = [sample_average, weighted_average]
    for m, method in enumerate(methods):
        env = MultiArmedBandit(n_arms, mu, sigma)
        for step_id in range(n_steps):
            action = method.select_action(epsilon)
            optimal = env.is_optimal(action)
            reward = env.reward(action)
            method.update_Q(action, reward)
            env.random_walk()
            
            rewards[step_id, run_id, m] = reward
            optimals[step_id, run_id, m] = optimal
            
line_plot(rewards, 'Average Reward', 'Ex_2.5_avg_reward.png')      
line_plot(optimals, 'Optimal Action %', 'Ex_2.5_optimal_action.png') 
