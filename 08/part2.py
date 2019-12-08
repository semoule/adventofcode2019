#!/usr/bin/env python
# encoding: utf-8

import sys

## DATA
filename = "./input.txt"

## FUNCTIONS

# draw image
def draw_layer(layer):
  for i in range(0, 6):
    line = ''
    for j in range(i * 25, 25 + i * 25):
      if layer[j] == 0:
        pixel = ' '
      elif layer[j] == 2:
        pixel = ' '
      else:
        pixel = '1'
      line = line + pixel
    print(line)
  return

# layer superposition
def compute_layer(layer1, layer2):
  newlayer = []
  for i in range(0,len(layer1)):
    if layer1[i] == 2:
      visible = layer2[i]
    else:
      visible = layer1[i]
    newlayer.append(visible)
  return newlayer


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
#print("Layer count : ", layer_count)

# digit per layer
digit_per_layer = int(len(digit_list) / (len(digit_list) / (25 * 6)))
#print("digit per layer : ",digit_per_layer)

# create list of layer containing list of digits
layer_list = []
for i in range(0, layer_count):
  layer_list.append([])
  for j in range(i * digit_per_layer, (digit_per_layer + i * digit_per_layer)):
    layer_list[i].append(digit_list[j])

# rendering
render = layer_list[0]
for i in range(0, len(layer_list)-1):
  render = compute_layer(render,layer_list[i+1])

# drawing
image = draw_layer(render)