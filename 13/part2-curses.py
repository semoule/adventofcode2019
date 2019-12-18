#!/usr/bin/env python
# encoding: utf-8

import itertools
from time import sleep 
from os import system, name
import sys, select
import curses, time


## DATA
dataset = [2, 380, 379, 385, 1008, 2249, 380030, 381, 1005, 381, 12, 99, 109, 2250, 1102, 1, 0, 383, 1101, 0, 0, 382, 20101, 0, 382, 1, 20101, 0, 383, 2, 21102, 1, 37, 0, 1106, 0, 578, 4, 382, 4, 383, 204, 1, 1001, 382, 1, 382, 1007, 382, 35, 381, 1005, 381, 22, 1001, 383, 1, 383, 1007, 383, 23, 381, 1005, 381, 18, 1006, 385, 69, 99, 104, -1, 104, 0, 4, 386, 3, 384, 1007, 384, 0, 381, 1005, 381, 94, 107, 0, 384, 381, 1005, 381, 108, 1105, 1, 161, 107, 1, 392, 381, 1006, 381, 161, 1102, 1, -1, 384, 1105, 1, 119, 1007, 392, 33, 381, 1006, 381, 161, 1102, 1, 1, 384, 20101, 0, 392, 1, 21102, 21, 1, 2, 21102, 0, 1, 3, 21101, 0, 138, 0, 1105, 1, 549, 1, 392, 384, 392, 21002, 392, 1, 1, 21102, 21, 1, 2, 21101, 3, 0, 3, 21102, 1, 161, 0, 1105, 1, 549, 1101, 0, 0, 384, 20001, 388, 390, 1, 20101, 0, 389, 2, 21102, 180, 1, 0, 1105, 1, 578, 1206, 1, 213, 1208, 1, 2, 381, 1006, 381, 205, 20001, 388, 390, 1, 21002, 389, 1, 2, 21102, 1, 205, 0, 1105, 1, 393, 1002, 390, -1, 390, 1102, 1, 1, 384, 21001, 388, 0, 1, 20001, 389, 391, 2, 21101, 0, 228, 0, 1105, 1, 578, 1206, 1, 261, 1208, 1, 2, 381, 1006, 381, 253, 21001, 388, 0, 1, 20001, 389, 391, 2, 21101, 0, 253, 0, 1106, 0, 393, 1002, 391, -1, 391, 1101, 0, 1, 384, 1005, 384, 161, 20001, 388, 390, 1, 20001, 389, 391, 2, 21101, 0, 279, 0, 1106, 0, 578, 1206, 1, 316, 1208, 1, 2, 381, 1006, 381, 304, 20001, 388, 390, 1, 20001, 389, 391, 2, 21102, 304, 1, 0, 1105, 1, 393, 1002, 390, -1, 390, 1002, 391, -1, 391, 1101, 0, 1, 384, 1005, 384, 161, 20101, 0, 388, 1, 21001, 389, 0, 2, 21102, 1, 0, 3, 21102, 1, 338, 0, 1106, 0, 549, 1, 388, 390, 388, 1, 389, 391, 389, 20101, 0, 388, 1, 21001, 389, 0, 2, 21102, 1, 4, 3, 21101, 365, 0, 0, 1106, 0, 549, 1007, 389, 22, 381, 1005, 381, 75, 104, -1, 104, 0, 104, 0, 99, 0, 1, 0, 0, 0, 0, 0, 0, 260, 15, 18, 1, 1, 17, 109, 3, 21202, -2, 1, 1, 21202, -1, 1, 2, 21101, 0, 0, 3, 21102, 414, 1, 0, 1106, 0, 549, 21202, -2, 1, 1, 22101, 0, -1, 2, 21102, 1, 429, 0, 1106, 0, 601, 1201, 1, 0, 435, 1, 386, 0, 386, 104, -1, 104, 0, 4, 386, 1001, 387, -1, 387, 1005, 387, 451, 99, 109, -3, 2105, 1, 0, 109, 8, 22202, -7, -6, -3, 22201, -3, -5, -3, 21202, -4, 64, -2, 2207, -3, -2, 381, 1005, 381, 492, 21202, -2, -1, -1, 22201, -3, -1, -3, 2207, -3, -2, 381, 1006, 381, 481, 21202, -4, 8, -2, 2207, -3, -2, 381, 1005, 381, 518, 21202, -2, -1, -1, 22201, -3, -1, -3, 2207, -3, -2, 381, 1006, 381, 507, 2207, -3, -4, 381, 1005, 381, 540, 21202, -4, -1, -1, 22201, -3, -1, -3, 2207, -3, -4, 381, 1006, 381, 529, 21202, -3, 1, -7, 109, -8, 2105, 1, 0, 109, 4, 1202, -2, 35, 566, 201, -3, 566, 566, 101, 639, 566, 566, 2101, 0, -1, 0, 204, -3, 204, -2, 204, -1, 109, -4, 2105, 1, 0, 109, 3, 1202, -1, 35, 593, 201, -2, 593, 593, 101, 639, 593, 593, 21001, 0, 0, -2, 109, -3, 2105, 1, 0, 109, 3, 22102, 23, -2, 1, 22201, 1, -1, 1, 21101, 0, 409, 2, 21102, 1, 437, 3, 21102, 1, 805, 4, 21102, 1, 630, 0, 1106, 0, 456, 21201, 1, 1444, -2, 109, -3, 2106, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 0, 0, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 0, 1, 1, 0, 0, 2, 2, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 0, 0, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 2, 0, 2, 2, 0, 0, 0, 1, 1, 0, 2, 0, 2, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2, 2, 0, 0, 2, 0, 2, 0, 0, 0, 1, 1, 0, 2, 0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 2, 0, 2, 2, 2, 0, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 1, 1, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 2, 2, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 1, 1, 0, 2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 0, 2, 2, 0, 0, 2, 2, 0, 2, 2, 0, 2, 0, 2, 2, 0, 2, 2, 0, 2, 0, 1, 1, 0, 2, 0, 0, 2, 2, 0, 2, 2, 2, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 0, 1, 1, 0, 0, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 0, 2, 2, 2, 2, 0, 2, 0, 2, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 1, 1, 0, 0, 2, 2, 0, 0, 0, 2, 0, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0, 2, 2, 0, 2, 2, 0, 0, 0, 2, 2, 0, 0, 1, 1, 0, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 2, 0, 2, 2, 0, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 0, 1, 1, 0, 0, 2, 2, 0, 0, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 2, 2, 0, 0, 1, 1, 0, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0, 0, 2, 0, 1, 1, 0, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 2, 2, 0, 1, 1, 0, 2, 2, 0, 2, 2, 2, 0, 2, 0, 2, 0, 0, 0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 2, 2, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 50, 83, 17, 51, 29, 67, 27, 74, 3, 96, 21, 38, 14, 55, 71, 75, 15, 64, 69, 72, 2, 30, 70, 52, 29, 61, 96, 52, 48, 79, 27, 36, 90, 39, 21, 41, 55, 56, 8, 7, 13, 5, 39, 49, 22, 52, 66, 77, 95, 3, 46, 35, 75, 31, 31, 96, 86, 23, 72, 71, 27, 20, 6, 58, 70, 37, 48, 67, 24, 58, 27, 92, 29, 82, 30, 53, 76, 42, 54, 65, 62, 4, 57, 20, 42, 57, 25, 16, 76, 48, 77, 36, 61, 22, 31, 65, 88, 7, 50, 34, 54, 7, 1, 38, 62, 62, 83, 33, 70, 73, 46, 14, 89, 23, 98, 14, 28, 75, 79, 15, 3, 98, 79, 3, 4, 28, 22, 5, 73, 63, 60, 66, 45, 36, 96, 80, 48, 23, 97, 98, 79, 79, 82, 45, 72, 6, 68, 17, 51, 13, 34, 27, 95, 84, 59, 41, 40, 40, 13, 86, 21, 92, 37, 30, 54, 59, 48, 94, 63, 37, 53, 2, 62, 87, 47, 42, 28, 60, 48, 97, 61, 68, 59, 39, 31, 22, 88, 34, 72, 54, 11, 89, 34, 68, 35, 71, 5, 68, 97, 37, 43, 41, 80, 42, 39, 91, 94, 41, 56, 18, 10, 76, 69, 39, 4, 4, 11, 14, 32, 45, 85, 65, 57, 51, 72, 70, 53, 71, 29, 9, 78, 24, 31, 16, 9, 63, 40, 10, 26, 73, 69, 45, 72, 15, 98, 83, 59, 3, 21, 72, 97, 19, 74, 69, 61, 61, 62, 55, 91, 28, 4, 25, 27, 61, 89, 91, 16, 56, 11, 63, 93, 25, 88, 17, 12, 44, 69, 92, 90, 41, 6, 30, 3, 89, 1, 17, 21, 56, 93, 2, 47, 14, 14, 92, 21, 52, 83, 36, 36, 11, 97, 6, 57, 53, 97, 88, 48, 70, 53, 94, 84, 79, 56, 2, 35, 36, 68, 18, 97, 60, 75, 85, 30, 4, 89, 14, 45, 13, 88, 41, 16, 59, 52, 8, 47, 50, 76, 93, 36, 87, 22, 65, 36, 32, 56, 63, 31, 97, 51, 70, 4, 49, 37, 5, 27, 48, 16, 48, 79, 92, 55, 3, 94, 35, 46, 79, 4, 92, 46, 22, 87, 21, 88, 50, 36, 82, 67, 40, 63, 97, 69, 91, 63, 98, 68, 2, 17, 3, 87, 59, 71, 87, 18, 30, 13, 86, 87, 84, 39, 14, 63, 49, 83, 57, 5, 66, 11, 61, 81, 9, 81, 52, 62, 47, 32, 86, 28, 96, 4, 57, 4, 57, 95, 91, 71, 91, 57, 1, 16, 46, 40, 38, 62, 7, 85, 87, 76, 22, 43, 23, 77, 85, 73, 37, 37, 90, 53, 7, 25, 30, 57, 98, 73, 66, 56, 48, 19, 74, 53, 4, 65, 38, 94, 9, 22, 55, 67, 89, 81, 96, 36, 42, 3, 17, 73, 28, 56, 40, 42, 72, 28, 20, 4, 49, 2, 14, 18, 10, 34, 78, 13, 13, 65, 6, 55, 47, 97, 37, 24, 51, 88, 42, 22, 60, 35, 2, 10, 27, 37, 13, 51, 53, 24, 26, 81, 62, 68, 30, 25, 34, 9, 29, 51, 6, 22, 76, 21, 40, 38, 97, 7, 64, 31, 80, 64, 10, 89, 69, 50, 64, 74, 94, 22, 75, 30, 41, 48, 58, 77, 70, 48, 22, 86, 10, 35, 82, 84, 8, 23, 28, 21, 79, 98, 43, 34, 19, 71, 39, 80, 35, 37, 81, 33, 8, 35, 56, 68, 23, 2, 38, 32, 32, 86, 60, 37, 42, 53, 10, 16, 5, 45, 92, 20, 78, 90, 25, 19, 94, 44, 7, 81, 22, 3, 4, 37, 14, 26, 3, 42, 92, 22, 44, 58, 28, 63, 41, 81, 94, 85, 2, 96, 63, 67, 87, 42, 55, 27, 22, 94, 14, 86, 19, 88, 65, 93, 91, 11, 47, 67, 98, 28, 6, 43, 46, 41, 33, 27, 84, 96, 39, 40, 54, 81, 39, 68, 85, 79, 48, 59, 27, 68, 34, 51, 36, 64, 8, 54, 44, 17, 58, 54, 83, 17, 56, 79, 57, 5, 52, 25, 8, 73, 23, 63, 89, 91, 72, 74, 4, 12, 97, 67, 6, 67, 88, 52, 92, 97, 28, 75, 85, 64, 29, 20, 5, 35, 7, 54, 38, 14, 93, 62, 59, 74, 93, 86, 91, 82, 23, 83, 1, 35, 5, 21, 18, 71, 7, 39, 8, 32, 68, 57, 95, 67, 39, 19, 98, 89, 17, 87, 37, 78, 54, 36, 22, 30, 35, 68, 95, 61, 31, 72, 86, 85, 33, 12, 81, 91, 1, 23, 63, 91, 34, 5, 86, 70, 65, 69, 72, 20, 84, 38, 13, 94, 47, 22, 40, 85, 15, 18, 95, 26, 68, 63, 59, 38, 73, 24, 69, 31, 21, 87, 90, 66, 87, 84, 30, 79, 76, 55, 33, 55, 33, 94, 7, 55, 380030]


## FUNCTIONS
def get_opcode(rawvalue):
  if len(str(rawvalue)) == 1:
    opcode = rawvalue
  else:
    opcode = int(str(rawvalue)[-2:])
  return opcode

def get_opmode(rawvalue):
  if len(str(rawvalue)) == 5:
    opmode = str(rawvalue)[:3]
  elif len(str(rawvalue)) == 4:
    opmode = "0" + str(rawvalue)[:2]
  elif len(str(rawvalue)) == 3:
    opmode = "00" + str(rawvalue)[:1]
  else:
    opmode = "000"
  return opmode

def get_value(dataset, pointer, opmode, opindex, relativebase):
  value = None
  if opmode[opindex] == "0":
    try:
      value = int(dataset[int(dataset[pointer + 3 - opindex])])
    except:
      value = 0
  elif opmode[opindex] == "1":
    value = int(dataset[pointer + 3 - opindex])
  elif opmode[opindex] == "2":
    value = int(dataset[int(dataset[pointer + 3 - opindex]) + relativebase])
  else:
    print("opmode error : ", opmode)
  return value

def get_index(dataset, pointer, opmode, opindex, relativebase):
  index = None
  if opmode[opindex] == "0":
    index = int(dataset[pointer + 3 - opindex])
  elif opmode[opindex] == "1":
    index = pointer + 3 - opindex
  elif opmode[opindex] == "2":
    index = int(dataset[pointer + 3 - opindex]) + relativebase
  else:
    print("opmode error : ", opmode)
  return index

def intcode(dataset, pointer, rbase, inval, stdscr):
  outindex = 0
  lastmove = False
  outval = [0, 0, 0]
  relativebase = rbase
  game_initialized = False

  opcode = get_opcode(dataset[pointer])
  opmode = get_opmode(dataset[pointer])

#  print(dataset, pointer, rbase)
#  print("relativebase : ", relativebase)
#  print()
  while opcode != 99:
    # Opcode 1 adds together numbers read from two positions and stores the result in a third position.
    if opcode == 1:
      val1 = get_value(dataset, pointer, opmode, 2, relativebase)
      val2 = get_value(dataset, pointer, opmode, 1, relativebase)
      index3 = get_index(dataset, pointer, opmode, 0, relativebase)
      dataset[index3] = val1 + val2
      pointer += 4
  
    # Opcode 1 multiply together numbers read from two positions and stores the result in a third position.
    elif opcode == 2:
      val1 = get_value(dataset, pointer, opmode, 2, relativebase)
      val2 = get_value(dataset, pointer, opmode, 1, relativebase)
      index3 = get_index(dataset, pointer, opmode, 0, relativebase)
      dataset[index3] = val1 * val2
      pointer += 4

    # Opcode 3 takes a single integer as input and saves it to the position given by its only parameter.
    elif opcode == 3:
      inval, stdscr = joystick(stdscr)
      index1 = get_index(dataset, pointer, opmode, 2, relativebase)
      dataset[index1] = int(inval)
      pointer += 2
      game_initialized = True

    # Opcode 4 outputs the value of its only parameter.
    elif opcode == 4:
      index1 = get_index(dataset, pointer, opmode, 2, relativebase)
      outval[outindex] = dataset[index1]
      outindex += 1
      pointer += 2
      if outindex == 3:
        break

    #Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    elif opcode == 5:
      val1 = get_value(dataset, pointer, opmode, 2, relativebase)
      val2 = get_value(dataset, pointer, opmode, 1, relativebase)
      if val1 != 0:
        pointer = val2
      else:
        pointer += 3
    
    #Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    elif opcode == 6:
      val1 = get_value(dataset, pointer, opmode, 2, relativebase)
      val2 = get_value(dataset, pointer, opmode, 1, relativebase)
      if val1 == 0:
        pointer = val2
      else:
        pointer += 3
    
    #Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    elif opcode == 7:
      val1 = get_value(dataset, pointer, opmode, 2, relativebase)
      val2 = get_value(dataset, pointer, opmode, 1, relativebase)
      index3 = get_index(dataset, pointer, opmode, 0, relativebase)
      if val1 < val2:
        dataset[index3] = 1
      else:
        dataset[index3] = 0
      pointer += 4
  
    #Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    elif opcode == 8:
      val1 = get_value(dataset, pointer, opmode, 2, relativebase)
      val2 = get_value(dataset, pointer, opmode, 1, relativebase)
      index3 = get_index(dataset, pointer, opmode, 0, relativebase)
      if val1 == val2:
        dataset[index3] = 1
      else:
        dataset[index3] = 0
      pointer += 4

    #Opcode 9 adjusts the relative base by the value of its only parameter. The relative base increases (or decreases, if negative value) by the value of the parameter.
    elif opcode == 9:
      val1 = get_value(dataset, pointer, opmode, 2, relativebase)
      relativebase += val1
      pointer += 2

    else:
      print("error opcode : ",opcode)
  
    opcode = get_opcode(dataset[pointer])
    opmode = get_opmode(dataset[pointer])
  
  if opcode == 99:
    lastmove = True
  
  return outval[0], outval[1], outval[2], dataset, pointer, relativebase, lastmove, stdscr

def get_representation(tile):
  # 0 is an empty tile. No game object appears in this tile.
  # 1 is a wall tile. Walls are indestructible barriers.
  # 2 is a block tile. Blocks can be broken by the ball.
  # 3 is a horizontal paddle tile. The paddle is indestructible.
  # 4 is a ball tile. The ball moves diagonally and bounces off objects.
  #get_last_tile(tile_list, tile)

  if tile[2] == 0:
    representation = ' '
  elif tile[2] == 1:
    representation = '|'
  elif tile[2] == 2:
    representation = '*'
  elif tile[2] == 3:
    representation = '-'
  elif tile[2] == 4:
    representation = 'o'
  else:
    # score
    if tile[0] == -1 and tile[1] == 0:
      representation = str(tile[2])
    else:
      print("tile error")
      representation = ' '
  return representation

def joystick(stdscr):
  time.sleep(1)
  c = ""
  outval = 0
  try:
     c = stdscr.getkey()
     if c == "b": #curses.KEY_LEFT:
       outval = -1
     elif c == "n": #curses.KEY_RIGHT:
       outval = 1
  except Exception as e:
     pass

  return outval,stdscr

## MAIN
# extend dataset memory
for i in range(0, 2000):
  dataset.append(0)

stdscr = curses.initscr()
stdscr.nodelay(1)
curses.noecho()
stdscr.keypad(True)
curses.cbreak()

game_exit = False
game_initialized = False
pointer = 0
relativebase = 0
tile_list = []
inval = 0

while not game_exit:
  result = intcode(dataset, pointer, relativebase, inval, stdscr)
  tile = (result[0], result[1], result[2])
  dataset = result[3]
  pointer = result[4]
  relativebase = result[5]
  game_exit = result[6]
  stdscr = result[7]

  tile_list.append(tile)

  stdscr.move(0, 0)
  for tile in tile_list:
    tile_representation = get_representation(tile)
    if len(tile_representation) == 1:
      stdscr.addch(abs(tile[1]), abs(tile[0]), tile_representation)
    else:
      stdscr.addstr(abs(tile[1]), abs(tile[0]), tile_representation)