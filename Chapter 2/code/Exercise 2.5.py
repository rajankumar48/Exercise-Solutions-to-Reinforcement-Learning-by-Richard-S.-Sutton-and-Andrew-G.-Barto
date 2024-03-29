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
#

class MultiArmedBandit(object):
    def __init__(self, n_arms, mu, sigma):
        self.n_arms = n_arms
        self.mu = mu
        self.sigma = sigma
        self.q_star = np.zeros(n_arms)
    
    def random_walk(self):
        self.q_star += np.random.normal(self.mu, self.sigma, self.n_arms)
        
    def is_optimal(self, action):
        return action == np.argmax(self.q_star)
    
    def reward(self, action):
        return np.random.normal(self.q_star[action], 1, 1)

#%% Create estimators

class Estimator():
    def __init__(self, Q, epsilon):
        self.epsilon = epsilon
        self.Q = Q.copy()
        self.n_arms = len(Q)
        
    def select_action(self):
        if np.random.rand() < self.epsilon:
            return np.random.randint(0, self.n_arms - 1)
            
        else:
            return np.random.choice(np.flatnonzero(self.Q == self.Q.max())) # random tie breaker
            # return np.argmax(self.Q)

class SampleAverage(Estimator):
    def __init__(self, Q, epsilon):
        super().__init__(Q, epsilon)
        self.arm_count = np.zeros(len(Q))
        # self.Q = Q
    
    def update_Q(self, action, R):
        self.arm_count[action] += 1
        self.Q[action] = self.Q[action] + (R - self.Q[action])/self.arm_count[action]
        # return self.Q
        

class WeightedAverage(Estimator):
    def __init__(self, Q, epsilon, alpha):
        super().__init__(Q, epsilon)
        self.alpha = alpha
        # self.Q = Q
    
    def update_Q(self, action, R):
        self.Q[action] = self.Q[action] + self.alpha*(R - self.Q[action])
        # return self.Q
    
def line_plot(data, ylabel, fig_name):
    mean_data = np.mean(data, axis = 1)
    mean_data = pd.DataFrame(mean_data, columns = ['Sample Average', 'Weighted Average'])
    mean_data['Steps'] = mean_data.index + 1
    data_melt = pd.melt(mean_data, id_vars = ['Steps'], value_vars = mean_data.columns.drop('Steps'))
    fig, ax = plt.subplots(figsize = (10, 5))
    sns.lineplot(data = data_melt, x = 'Steps', y = 'value', hue = 'variable')
    ax.set_ylabel(ylabel)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles[1:], labels=labels[1:], loc = 'lower right')
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

n_estimators = 2

rewards = np.empty((n_steps, n_runs, n_estimators))
optimals = np.empty((n_steps, n_runs, n_estimators))
initial_Q = np.zeros(n_arms)
Q = np.zeros(n_arms)

for run_id in tqdm(range(n_runs)):
    sample_average = SampleAverage(initial_Q, epsilon)
    weighted_average = WeightedAverage(initial_Q, epsilon, alpha)
    estimators = [sample_average, weighted_average]
    
    for i, estimator in enumerate(estimators):
        env = MultiArmedBandit(n_arms, mu, sigma)
        
        for step_id in range(n_steps):
            action = estimator.select_action()
            optimal = env.is_optimal(action)
            reward = env.reward(action)
            estimator.update_Q(action, reward)
            env.random_walk()
            
            rewards[step_id, run_id, i] = reward
            optimals[step_id, run_id, i] = optimal
            
line_plot(rewards, 'Average Reward', 'Ex_2.5_avg_reward')      
line_plot(optimals, 'Optimal Action %', 'Ex_2.5_optimal_action') 
