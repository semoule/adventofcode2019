#!/usr/bin/env python
# encoding: utf-8

import sys
import math

## DATA
filepath = "./data1.txt"

## FUNCTIONS
def check_sight(candidate, anotherone,angle_list):
  angle = get_angle(candidate, anotherone)
  if candidate == anotherone:
    return False,angle_list
  if angle in angle_list:
    return False,angle_list
  else:
    angle_list.append(angle)
    return True,angle_list

def get_angle(candidate, anotherone):
  angle_radian = math.atan2(anotherone[1] - candidate[1], anotherone[0] - candidate[0])
  angle_degrees = math.degrees(angle_radian)
  #print(candidate,anotherone,angle_degrees)
  return angle_degrees

def get_distance(candidate, anotherone):  
  dist = math.sqrt((anotherone[0] - candidate[0])**2 + (anotherone[1] - candidate[1])**2)  
  return dist

## MAIN
asteroid_list = []
y = 0
with open(filepath) as fp:
  line = fp.readline()
  while line:
    x = 0
    for i in range(0, len(line)):
      if line[i] == '#':
        asteroid_list.append((x, y))
      x = x + 1
    y = y + 1
    line = fp.readline()

#print(asteroid_list)

asteroid_sight_list = []
angle_list = []

# get best place
for candidate in asteroid_list:
  sight_count = 0
  angle_list = []
  for anotherone in asteroid_list:
    result = check_sight(candidate, anotherone, angle_list)
    insight = result[0]
    angle_list = result[1]
    if insight is True:
      sight_count += 1
  asteroid_sight_list.append((candidate, sight_count))

asteroid_sight_list.sort(key=lambda x: x[1], reverse=True)
print("best asteroid : ", asteroid_sight_list[0][0], " with count : ", asteroid_sight_list[0][1])

# install laser on best place
laser = asteroid_sight_list[0][0]

# create list of asteroid with angle and distance from laser
asteroid_info_list = []
for asteroid in asteroid_list:
  angle = get_angle(laser, asteroid)
  distance = get_distance(laser, asteroid)
  if asteroid != laser:
    asteroid_info_list.append((asteroid, angle, distance))
  print(asteroid,angle,distance)

#print(asteroid_info_list)
#asteroid_info_list.sort(key=lambda x: (x[1], x[2]))
print()
print(asteroid_info_list)

# create angle list
angle_list = set(x[1] for x in asteroid_info_list)
print()
print("angle_list", angle_list)
print()

# create list of asteroid for each angle
asteroid_by_angle_list = []
i = 0
for angle in sorted(angle_list):
  matches = list(filter(lambda x: x[1] == angle, asteroid_info_list))  
  asteroid_by_angle_list.append(matches)
  #print(angle,matches)

print(asteroid_by_angle_list)