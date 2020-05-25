#!/usr/bin/python3
from math import pi


def volume(h , r = 10):
    liquid = ((4 * pi * r**3) / 3) - (pi * h**2 * (3 * r - h) / 3)
    return liquid
print(volume(2))