import os
import hashlib
import random
import re
import subprocess

from Fraction import Fraction 
from Book import Book
from Library import Library
from StringFormatter import StringFormatter

import GUI3
import GUI5

def Ex1():
    frac = Fraction(7,2)
    print(frac)
    print(-frac) # выводит -7/2
    print(~frac) # выводит 2/7
    print(frac**2) # выводит 49/4
    print(float(frac)) # выводит 3.5
    print(int(frac)) # выводит 3

def Ex2():
    lib = Library(1, "51 Some str., NY")
    lib += Book("Leo Tolstoi", "War and Peace")
    lib += Book("Charles Dickens", "David Copperfield")
    for book in lib:
        # вывод в виде: [1] L.Tolstoi "War and Peace"
        print(book)
        # вывод в виде: ["War", "Peace"]
        print(book.tag())
def Ex3():
    GUI3.main()

def Ex4():
    string = "Azaz sis somarolinto go go go trenyzi12 keks koks kaks 74rus 123 321 pas123sajiri"
    print(StringFormatter.del_worlds(string, 5))
    print(StringFormatter.replace(string)) 
    print(StringFormatter.set_spaces(string))
    print(StringFormatter.sort_size(string))
    print(StringFormatter.sort(string))

def Ex5():
    GUI5.main()

if __name__ == "__main__":
    Ex5()
