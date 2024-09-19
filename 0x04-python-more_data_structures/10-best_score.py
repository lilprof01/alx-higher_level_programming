#!/usr/bin/python3
def best_score(a_dictionary):
    max_key = None
    max_value = 0
    if not a_dictionary:
        return None
    else:
        for k, v in a_dictionary.items():
            if v > max_value:
                max_value = v
                max_key = k
        return max_key
