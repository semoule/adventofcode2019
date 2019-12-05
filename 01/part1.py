#!/usr/bin/env python
# encoding: utf-8

import sys
import math

total = 0

## FUNCTIONS
def calcul(line):
  valret = math.trunc(int(line) / 3) - 2
  print(valret)
  return valret

## MAIN
with sys.stdin as my_file:
    for line in my_file:
        total = total + calcul(line)

print(total)