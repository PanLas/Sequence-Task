# -*- coding: utf-8 -*-
"""
@author: Stefan Kasperzack

Plots for hailstone sequence any key-value pair m = {1, 2, 3, ...} and
corresponding counts number of steps until sequence reached one for first time.
"""

import matplotlib.pyplot as plt
from a_step_count import number_steps_to_reach_one

interval_m = range(1, 10000 + 1)
number_steps_to_interval = []
for number_m in interval_m:
    number_of_steps = number_steps_to_reach_one(number_m)
    number_steps_to_interval.append(number_of_steps)

plt.scatter(interval_m, number_steps_to_interval, s=2)
plt.xlabel("m")
plt.ylabel("Number of steps")
plt.title("Number of steps for each m $\in$ [1, 10000]")
plt.show()
