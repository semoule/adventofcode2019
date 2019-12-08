#!/usr/bin/env python
# encoding: utf-8

import sys

## DATA
filename = "./input.txt"

## MAIN
digit_list = []

# load digit in a list
with open(filename) as f:
  while True:
    c = f.read(1)
    if not c:
      break
    if str(c) != '\n':
      digit_list.append(int(c))
f.close()

# Layer count
layer_count = int(len(digit_list) / (25 * 6))
print("Layer count : ", layer_count)

# digit per layer
digit_per_layer = int(len(digit_list) / (len(digit_list) / (25 * 6)))
print("digit per layer : ",digit_per_layer)

# create list of layer containing list of digits
layer_list = []
for i in range(0, layer_count):
  layer_list.append([])
  for j in range(i * digit_per_layer, (digit_per_layer + i * digit_per_layer)):
    layer_list[i].append(digit_list[j])

# create list of zero count
zerocount_list = []
for i in range(0, layer_count):
  zerocount_list.append(layer_list[i].count(0))

# layer index with fewer 0
layerindex = zerocount_list.index(min(zerocount_list))

# number of 1 * number of 2
answer = layer_list[layerindex].count(1) * layer_list[layerindex].count(2)
print(answer)