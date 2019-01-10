#!/bin/python3
#Author - Gaurav Dua
#Q1. https://www.hackerrank.com/challenges/encryption/problem
#This code will run on hackerrank link only, to check it on system, please copy encryption() definition and run it

import math
import os

def encryption(s):
    s = s.replace(" ", "")
    strLen = len(s)
    low = math.floor(math.sqrt(strLen))
    high = math.ceil(math.sqrt(strLen))
    if low * high < strLen :
        low = high
    newStr = ""
    for i in range(high):
        for j in range(high):
            if (i+high*j)<strLen:
                newStr += s[i+high*j]
        newStr += " "
    newStr = newStr.rstrip()
    return newStr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
