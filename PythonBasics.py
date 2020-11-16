#Python Review 1: Introduction
#!/bin/python3

import math
import os
import random
import re
import sys

def ifelse():
    n = int(input().strip())
    if (n%2==0):
        if (n>=2 and n<=5):
            print("Not Weird")
        elif (n>=6 and n<=20):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")

def is_leap(year):
    # Write your logic here
    leap = False
    # Write your logic here
    if year%4==0:
        if year%100==0:
            leap=False
            if year%400==0:
                leap=True
        else:
            leap=True   
    return leap
def leap():
    year = int(input())
    print(is_leap(year))