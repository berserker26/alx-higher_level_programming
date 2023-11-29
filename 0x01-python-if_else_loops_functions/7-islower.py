#!/usr/bin/python3
def islower(c):
    is_lwr_upr = ord(c)
    if is_lwr_upr < 123 and is_lwr_upr > 96:
        return True
    else:
        return False
