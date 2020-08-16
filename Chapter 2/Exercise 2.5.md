# Exercise 2.5

### *(Programming)* Design and conduct an experiment to demonstrate the difficulties that sample-average methods have for non-stationary problems. Use a modified version of the 10-armed testbed in which all the q*(a) start out equal and then take independent random walks (say by adding a normally distributed increment with mean zero and standard deviation 0.01 to all the q*(a) on each step. Prepare plots like Figure 2.2 for an action-value method using sample averages, incrementally computed, and another action-value method using a constant step-size parameter, α = 0.1. Use ε = 0.1 and longer runs, say of 10,000 steps.

Weighted average method with constant step size overcomes the challenge of selecting optimal action compared to sample average method, hence increases the chance of getting better reward (as shown in the below figures).

Please refer code code/Exercise 2.5.py

![AverageReward](resources/Ex_2_5_avg_reward.png)

![OptimalAction](resources/Ex_2_5_optimal_action.png)
