#!/usr/bin/env python
# encoding: utf-8

import sys
import math
from os import system, name 
from time import sleep 

## DATA
filepath = "./data.txt"

## FUNCTIONS

# check insight
def check_sight(candidate, anotherone,angle_list):
  angle = get_angle(candidate, anotherone)
  if candidate == anotherone:
    return False,angle_list
  if angle in angle_list:
    return False,angle_list
  else:
    angle_list.append(angle)
    return True,angle_list

# get angle between 2 asteroids
def get_angle(candidate, anotherone):
  angle_radian = math.atan2(anotherone[1] - candidate[1], anotherone[0] - candidate[0])
  angle_degrees = math.degrees(angle_radian)
  return angle_degrees

# get distance between 2 asteroids
def get_distance(candidate, anotherone):  
  dist = math.sqrt((anotherone[0] - candidate[0])**2 + (anotherone[1] - candidate[1])**2)  
  return dist

# destroy closest asteroid for a given angle 
def destroy_asteroid(asteroid_pool,angle):
  asteroid = get_closer(asteroid_pool,angle)
  if asteroid != None:
    asteroid_pool.pop(asteroid_pool.index(asteroid))
  return asteroid_pool,asteroid

# find closest asteroid for a given angle
def get_closer(asteroid_pool,angle):
  # filter asteroid_pool by angle
  matches = list(filter(lambda x: x[1] == angle, asteroid_pool))
  if len(matches) == 0:
    asteroid = None
  else:
    # get lowest distance
    matches.sort(key=lambda x: x[2])
    asteroid = matches[0]
  return asteroid

# draw for fun :)
def draw(asteroid_field, maxx, maxy):
  sleep(0.5) 
  system('clear') 
  for x in range(0, maxx):
    line = ''
    for y in range(0, maxy):
      found = False
      for i in range(0, len(asteroid_field)):
        if (x, y) == asteroid_field[i][0]:
          found = True
          break
      if found == True:
        line = line + '#'
      else:
        line = line + ' '
    print(line)
  return


## MAIN
# read file and get asteroid coordinates
asteroid_list = []
y = 0
maxy=0
with open(filepath) as fp:
  line = fp.readline()
  maxx = len(line)
  
  while line:
    x = 0
    for i in range(0, len(line)):
      if line[i] == '#':
        asteroid_list.append((x, y))
      x = x + 1
    y = y + 1
    line = fp.readline()

maxy = y

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
  #print(asteroid,angle,distance)

# create angle list
angle_list = set(x[1] for x in asteroid_info_list)
new_angle_list = sorted(angle_list)

# prepare destroy loop
angle_index = new_angle_list.index(-90)
destroy_count = 0
asteroid_pool = asteroid_info_list

# destroy!
while len(asteroid_pool) > 1:
  draw(asteroid_pool, maxx, maxy)
  angle = new_angle_list[angle_index]
  result = destroy_asteroid(asteroid_pool,angle)
  asteroid_pool = result[0]
  destroyed_asteroid = result[1]
  if destroyed_asteroid != None:
    destroy_count += 1
    #print("destroy : ",destroy_count, destroyed_asteroid)
    angle_index +=1
    if angle_index == len(new_angle_list):
      angle_index = 0
  else:
    break
