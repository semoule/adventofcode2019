#!/usr/bin/env python
# encoding: utf-8

import itertools

## dataset
moon_list = [((3, -6, 6), (0, 0, 0)), ((10, 7, -9), (0, 0, 0)), ((-3, -7, 9), (0, 0, 0)), ((-8, 0, 4), (0, 0, 0))]
orig_state = [((3, -6, 6), (0, 0, 0)), ((10, 7, -9), (0, 0, 0)), ((-3, -7, 9), (0, 0, 0)), ((-8, 0, 4), (0, 0, 0))]

# test dataset
#moon_list = [((-1, 0, 2), (0, 0, 0)), ((2, -10, -7), (0, 0, 0)), ((4, -8, 8), (0, 0, 0)), ((3, 5, -1), (0, 0, 0))]

## functions
# update velocity
def compute_velocity(moon_a, moon_b):
  moon_a_pos_x = moon_a[0][0]
  moon_a_pos_y = moon_a[0][1]
  moon_a_pos_z = moon_a[0][2]
  moon_a_vel_x = moon_a[1][0]
  moon_a_vel_y = moon_a[1][1]
  moon_a_vel_z = moon_a[1][2]

  moon_b_pos_x = moon_b[0][0]
  moon_b_pos_y = moon_b[0][1]
  moon_b_pos_z = moon_b[0][2]
  moon_b_vel_x = moon_b[1][0]
  moon_b_vel_y = moon_b[1][1]
  moon_b_vel_z = moon_b[1][2]

  # x axis
  if moon_a_pos_x > moon_b_pos_x:
    moon_a_vel_x += -1
    moon_b_vel_x += 1
  elif moon_a_pos_x < moon_b_pos_x:
    moon_a_vel_x += 1
    moon_b_vel_x += -1

  # y axis
  if moon_a_pos_y > moon_b_pos_y:
    moon_a_vel_y += -1
    moon_b_vel_y += 1
  elif moon_a_pos_y < moon_b_pos_y:
    moon_a_vel_y += 1
    moon_b_vel_y += -1

  # z axis
  if moon_a_pos_z > moon_b_pos_z:
    moon_a_vel_z += -1
    moon_b_vel_z += 1
  elif moon_a_pos_z < moon_b_pos_z:
    moon_a_vel_z += 1
    moon_b_vel_z += -1

  return (((moon_a_pos_x,moon_a_pos_y,moon_a_pos_z),(moon_a_vel_x,moon_a_vel_y,moon_a_vel_z)),((moon_b_pos_x,moon_b_pos_y,moon_b_pos_z),(moon_b_vel_x,moon_b_vel_y,moon_b_vel_z)))

# update position of all moon with their velocity
def apply_velocity(moon_list):
  for moon in range(0, len(moon_list)):
    new_moon_pos_x = moon_list[moon][0][0] + moon_list[moon][1][0]
    new_moon_pos_y = moon_list[moon][0][1] + moon_list[moon][1][1]
    new_moon_pos_z = moon_list[moon][0][2] + moon_list[moon][1][2]
    new_moon_vel = moon_list[moon][1]
    moon_list[moon] = ((new_moon_pos_x,new_moon_pos_y,new_moon_pos_z),new_moon_vel)
  return moon_list

# compute moon energy
def compute_energy(moon):
  potential_energy = abs(moon[0][0]) + abs(moon[0][1]) + abs(moon[0][2])
  kinetic_energy = abs(moon[1][0]) + abs(moon[1][1]) + abs(moon[1][2])
  total = potential_energy * kinetic_energy
  return total

## main
step = 0
found = False
moon_index = list(range(0, len(moon_list)))

while not found:
  combination_list = list(itertools.combinations(moon_index, 2))
  for combo in combination_list:
    result = compute_velocity(moon_list[combo[0]], moon_list[combo[1]])
    moon_list[combo[0]] = result[0]
    moon_list[combo[1]] = result[1]
  moon_list = apply_velocity(moon_list)

  if set(moon_list) == set(orig_state):
    found = True
  step +=1

print(step)