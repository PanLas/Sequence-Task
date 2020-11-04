# -*- coding: utf-8 -*-
"""
@author: Stefan Kasperzack

Determines hailstone sequence for any natural number m and counts the number of
steps until the sequence reaches one for the first time.
"""

def number_steps_to_reach_one(initial_m):
    """Counts number of steps until sequence reaches one for first time

    Args:
        initial_m: An integer representing the start of sequence m

    Returns:
        number_of_steps: An integer representing the number of steps
    """
    current_number = initial_m
    number_of_steps = 0
    while current_number != 1:
        if current_number % 2 == 0: # If True: current_number is even,
            next_number = current_number // 2 # Floor division to get int.
        else: # else current_number is odd.
            next_number = current_number * 3 + 1
        current_number = next_number
        number_of_steps += 1
    return number_of_steps

def main():
    """Only executes if module is main (and not on import)

    Args:
        No arguments

    Returns:
        No returns
    """
    # Please set m (initial_m) as a whole number greater than 0.
    initial_m = 10
    number_of_steps = number_steps_to_reach_one(initial_m)
    print(f"For m = {initial_m},",
          f"{number_of_steps} steps are required to reach 1 for first time.")

if __name__ == "__main__":
    main()
