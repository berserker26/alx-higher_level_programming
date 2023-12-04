#!/usr/bin/python3
def no_c(my_string):
    noC = ""
    for letter in my_string:
        if letter != chr(99) and letter != chr(67):
            noC = noC + letter
    return (noC)
