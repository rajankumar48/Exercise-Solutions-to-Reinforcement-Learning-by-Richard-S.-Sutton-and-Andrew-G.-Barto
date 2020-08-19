# Exercise 2.8

### *UCB Spikes* In Figure 2.4 the UCB algorithm shows a distinct spike in performance on the 11th step. Why is this? Note that for your answer to be fully satisfactory it must explain both why the reward increases on the 11th step and why it decreases on the subsequent steps. Hint: if c = 1, then the spike is less prominent.

The selection of actions using UCB algorithm consists of 2 terms.

<img src="https://latex.codecogs.com/svg.latex?\Large&space;A_t=\arg\max_{a}\bigg[Q_t(a)+c\sqrt{\frac{\text{ln}t}{N_t(a)}}\bigg]" title="Equation10" />

For initial 10 steps, there will be atleast one action with N<sub>t</sub>(a) = 0. It would guide to select action at random amongst such actions. 

At step 11, all action has been selected exactly once, lnt and N<sub>t</sub>(a) become same of all actions which makes second term constant.
Now, the next action solely depends on action value estimates, Q<sub>t</sub>(a). 
In quest to maximize the reward, action with highest action value estimate is selected leading to sudden spike in reward.

In subsequent steps, N<sub>t</sub>(a) would not be same for all actions and there will be tradeoff b/w two terms with c as a weight factor for second term.
It would lead to exploration and hence decrease in average rewards.

If c = 1, the weightage to second term will be less and action would depend more on Q<sub>t</sub>(a), allowing more greedy actions, hence less prominent spike.
