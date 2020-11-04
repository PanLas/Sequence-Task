# -*- coding: utf-8 -*-
"""
@author: Stefan Kasperzack

Determines hailstone sequence for any m = {1, 2, 3, ...} and counts the number
of steps for each m until the sequence reaches one for the first time.
"""

from a_step_count import number_steps_to_reach_one

interval_m = range(1, 10000 + 1)
number_steps_to_interval = {}
for number_m in interval_m:
    number_of_steps = number_steps_to_reach_one(number_m)
    number_steps_to_interval[number_m] = number_of_steps
print("Key-value pairs of interval m and number of steps are (m: #steps):\n",
      number_steps_to_interval)
