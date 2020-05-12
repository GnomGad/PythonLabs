import os
import hashlib
import random
import re
import subprocess

from Fraction import Fraction 


def Ex1():
    frac = Fraction(7,2)
    print(frac)
    print(-frac) # выводит -7/2
    print(~frac) # выводит 2/7
    print(frac**2) # выводит 49/4
    print(float(frac)) # выводит 3.5
    print(int(frac)) # выводит 3

if __name__ == "__main__":
    Ex1()
