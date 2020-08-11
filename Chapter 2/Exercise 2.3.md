# Exercise 2.3

### In the comparison shown in Figure 2.2, which method will perform best in the long run in terms of cumulative reward and probability of selecting the best action? How much better will it be? Express your answer quantitatively.

As time t -> ∞, Q<sub>t</sub>(a) converge to q<sub>*</sub>(a) and probability of selecting the best action = (1 - ε) + ε * (probability of random action).

In 10-armed testbed, probability of random action = 0.1.

For ε = 0.01, probability of selecting best action = 0.99 + 0.01 * 0.1 = 0.991 or 99.1%

For ε = 0.1, probability of selecting best action = 0.9 + 0.1 * 0.1 = 0.91 or 91%

Hence, ε = 0.01 has 8.1% better probability of selecting best action.
