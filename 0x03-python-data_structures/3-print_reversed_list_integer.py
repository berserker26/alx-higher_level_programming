#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    lst_idx = 0
    for i in range(len(my_list)):
        lst_idx += 1
    while my_list:
        print("{:d}".format(my_list[lst_idx]))
