# Exercise 2.2

### _Bandit example_ Consider a k-armed bandit problem with k = 4 actions, denoted 1, 2, 3, and 4. Consider applying to this problem a bandit algorithm using ε-greedy action selectioni, sample average action-value estimates, and initial estimates of Q<sub>1</sub>(a) = 0, for all a. Suppose the initial sequence of actions and rewards is A<sub>1</sub> = 1, R<sub>1</sub> = 1, A<sub>2</sub> = 2, R<sub>2</sub> = 1, A<sub>3</sub> = 2, R<sub>3</sub> = 2, A<sub>4</sub> = 2, R<sub>4</sub> = 2, A<sub>5</sub> = 3, R<sub>5</sub> = 0. On some of these time steps the ε case may have ocurred, causing an action to be selected at random. On which time steps did this definitely occur? On which time steps could this possibly have occurred.

Let's initialize tha Q value of each action as below table:
|Iteration | a = 1 | a = 2 | a = 3 | a = 4 |
|:--------:|:-----:|:-----:|:-----:|:-----:|
| 0        | 0     | 0     | 0     | 0     |

Initially, Q value of all actions are same. Action taken is A<sub>1</sub> = 1. This could be exploration or exploitation.
Reward of this action, R<sub>1</sub> = 1. Hence Q table is updated as:

|Iteration | a = 1 | a = 2 | a = 3 | a = 4 |
|:--------:|:-----:|:-----:|:-----:|:-----:|
| 0        | 0     | 0     | 0     | 0     |
| 1        | 1     | 0     | 0     | 0     |

At this time step, a = 1 has highest Q value. It should take this action from greedy algorithm. However it takes A<sub>2</sub> = 2. Hence, it has selected random action and it is a case of exploration.
Reward of this action, R<sub>2</sub> = 1. Hence Q table is updated as:

|Iteration | a = 1 | a = 2 | a = 3 | a = 4 |
|:--------:|:-----:|:-----:|:-----:|:-----:|
| 0        | 0     | 0     | 0     | 0     |
| 1        | 1     | 0     | 0     | 0     |
| 2        | 1     | 1     | 0     | 0     |

At this time step, a = 1 and a = 2 has highest Q value. It should take one of these two actions and it took A<sub>3</sub> = 2. Hence, it could be exploitation or exploration.
Reward of this action, R<sub>3</sub> = 2. Hence Q table is updated as:

|Iteration | a = 1 | a = 2 | a = 3 | a = 4 |
|:--------:|:-----:|:-----:|:-----:|:-----:|
| 0        | 0     | 0     | 0     | 0     |
| 1        | 1     | 0     | 0     | 0     |
| 2        | 1     | 1     | 0     | 0     |
| 3        | 1     | 1.5   | 0     | 0     |

a = 2 has highest Q value, and it has taken this action. _Most likely_, it is a case of exploitation. I am saying _most likely_ because exploration could lead to this action.
Reward of this action, R<sub>4</sub> = 2. Hence Q table is updated as:

|Iteration | a = 1 | a = 2 | a = 3 | a = 4 |
|:--------:|:-----:|:-----:|:-----:|:-----:|
| 0        | 0     | 0     | 0     | 0     |
| 1        | 1     | 0     | 0     | 0     |
| 2        | 1     | 1     | 0     | 0     |
| 3        | 1     | 1.5   | 0     | 0     |
| 4        | 1     | 1.67  | 0     | 0     |

Similar to iteration 2, next action is exploitation and resulted to following Q table:

|Iteration | a = 1 | a = 2 | a = 3 | a = 4 |
|:--------:|:-----:|:-----:|:-----:|:-----:|
| 0        | 0     | 0     | 0     | 0     |
| 1        | 1     | 0     | 0     | 0     |
| 2        | 1     | 1     | 0     | 0     |
| 3        | 1     | 1.5   | 0     | 0     |
| 4        | 1     | 1.67  | 0     | 0     |
| 5        | 1     | 1.67  | 0     | 0     |
