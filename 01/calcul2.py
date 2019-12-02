#!/usr/bin/env python
# encoding: utf-8

import sys
import math

total = 0

## FUNCTIONS
def calcul(line):
  subtotal = 0
  valret = int(line)
  while valret > 0:
    valret = math.trunc(int(valret) / 3) - 2
    if valret > 0:
      subtotal = subtotal + valret
    print(valret)
  return subtotal

## MAIN
with sys.stdin as my_file:
    for line in my_file:
        total = total + calcul(line)

print(total)