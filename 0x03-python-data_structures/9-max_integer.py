#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return
    largest = my_list[0]
    for max in my_list:
        if max > largest:
            largest = max
    return largest
