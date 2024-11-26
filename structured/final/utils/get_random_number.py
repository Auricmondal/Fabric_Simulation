import random

def get_random_value(start_range=None, end_range=None):
    if start_range and end_range:
        return random.randint(start_range, end_range)
    return random.random()