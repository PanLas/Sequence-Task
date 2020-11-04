# -*- coding: utf-8 -*-
"""
@author: Stefan Kasperzack

Determines hailstone sequence for any m = {1, 2, 3, ...}, counts the number of
steps for each m until the sequence reaches one for the first time, and 
calculates the duration of the execution.
"""

import time

# Number of times function number_steps_to_reach_one() is executed.
number_executions = 10
interval_m = range(1, 10001)

def number_steps_to_reach_one(interval_m):
    """Counts for range num. of steps until sequence reaches one for first time

    Args:
        interval_m: An object representing values for m

    Returns:
        number_steps_to_interval: A dict representing the number of steps
    """
    number_steps_to_interval = {}
    for current_number in interval_m:
        number_m = current_number
        number_of_steps = 0
        m_already_in_dict = False
        while current_number != 1:
            if current_number % 2 == 0:
                current_number = current_number // 2
            else:
                current_number = current_number * 3 + 1
            number_of_steps += 1
            if current_number in number_steps_to_interval.keys():
                number_steps_to_interval[number_m] = number_steps_to_interval[current_number] + number_of_steps
                m_already_in_dict = True
                break
        if not m_already_in_dict:
            number_steps_to_interval[number_m] = number_of_steps
    return number_steps_to_interval


start_time = time.time()
for number in range(1, number_executions + 1):
    number_steps_to_interval = number_steps_to_reach_one(interval_m)
end_time = time.time()
total_time = end_time - start_time
print(f"Necessary time in sec. to execute function {number_executions} times:",
      total_time)
