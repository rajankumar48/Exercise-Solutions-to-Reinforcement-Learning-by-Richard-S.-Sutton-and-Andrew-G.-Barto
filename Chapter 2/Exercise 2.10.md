# Exercise 2.10

### Suppose you face a 2-armed bandit task whose true action values change randomly from time step to time step. Specifically, suppose that, for any time step, the true values of action 1 and 2 are respectively 0.1 and 0.2 with probability 0.5 (case A), and 0.9 and 0.8 with probability 0.5 (case B). If you are not able to tell which case you face at any step, what is the best expectation of success you can achieve and how should you behave to achieve it? Now suppose that on each step you are told whether you are facing case A or case B (although you still don't know the true action values). This is an associative search task. What is the best expectation of success you can achieve in this task, and how should you behave to achieve it?

Let's say a<sub>1</sub> and a<sub>2</sub> are two possible actions for each case.

For case A:

q<sub>*</sub>(a<sub>1</sub>) = 0.1

q<sub>*</sub>(a<sub>2</sub>) = 0.2

For case B:

q<sub>*</sub>(a<sub>1</sub>) = 0.9

q<sub>*</sub>(a<sub>2</sub>) = 0.8

Scenario I: Since we don't know which case we are facing, we can't keep record of individual estimates. 
Hence value of each action is weighted average of true action values with probability to select a case being weight

a1 = 0.1 * 0.5 + 0.9 * 0.5 = 0.5

a2 = 0.2 * 0.5 + 0.8 * 0.5 = 0.5

Since each action has equal value, we can achieve best expectation by randomly selecting any action.

Scenario II: We know which case we are facing (though we don't know the true action values).
We can keep the record of individual estimates and in long run we will learn which action to select for each case, i.e. action 2 for case A and action 1 for case B.

Best expectation of success:

0.2 * 0.5 + 0.9 * 0.5 = 0.55

