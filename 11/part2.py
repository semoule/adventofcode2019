#!/usr/bin/env python
# encoding: utf-8

import itertools
from time import sleep 

## DATA
dataset = [3, 8, 1005, 8, 318, 1106, 0, 11, 0, 0, 0, 104, 1, 104, 0, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 108, 1, 8, 10, 4, 10, 1002, 8, 1, 28, 1, 107, 14, 10, 1, 107, 18, 10, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 108, 1, 8, 10, 4, 10, 102, 1, 8, 58, 1006, 0, 90, 2, 1006, 20, 10, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 1001, 8, 0, 88, 2, 103, 2, 10, 2, 4, 7, 10, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 1001, 8, 0, 118, 1, 1009, 14, 10, 1, 1103, 9, 10, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 108, 0, 8, 10, 4, 10, 1002, 8, 1, 147, 1006, 0, 59, 1, 104, 4, 10, 2, 106, 18, 10, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 0, 10, 4, 10, 101, 0, 8, 181, 2, 4, 17, 10, 1006, 0, 36, 1, 107, 7, 10, 2, 1008, 0, 10, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 108, 0, 8, 10, 4, 10, 101, 0, 8, 217, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 0, 10, 4, 10, 101, 0, 8, 240, 1006, 0, 64, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 108, 0, 8, 10, 4, 10, 1002, 8, 1, 264, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 1001, 8, 0, 287, 1, 1104, 15, 10, 1, 102, 8, 10, 1006, 0, 2, 101, 1, 9, 9, 1007, 9, 940, 10, 1005, 10, 15, 99, 109, 640, 104, 0, 104, 1, 21102, 932700857236, 1, 1, 21101, 335, 0, 0, 1106, 0, 439, 21101, 0, 387511792424, 1, 21101, 346, 0, 0, 1106, 0, 439, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 1, 21101, 46372252675, 0, 1, 21102, 393, 1, 0, 1106, 0, 439, 21101, 97806162983, 0, 1, 21102, 404, 1, 0, 1105, 1, 439, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 0, 21102, 1, 825452438376, 1, 21101, 0, 427, 0, 1106, 0, 439, 21102, 709475586836, 1, 1, 21101, 0, 438, 0, 1106, 0, 439, 99, 109, 2, 22101, 0, -1, 1, 21101, 40, 0, 2, 21102, 1, 470, 3, 21102, 1, 460, 0, 1106, 0, 503, 109, -2, 2106, 0, 0, 0, 1, 0, 0, 1, 109, 2, 3, 10, 204, -1, 1001, 465, 466, 481, 4, 0, 1001, 465, 1, 465, 108, 4, 465, 10, 1006, 10, 497, 1101, 0, 0, 465, 109, -2, 2105, 1, 0, 0, 109, 4, 2102, 1, -1, 502, 1207, -3, 0, 10, 1006, 10, 520, 21102, 1, 0, -3, 21202, -3, 1, 1, 21202, -2, 1, 2, 21101, 0, 1, 3, 21101, 0, 539, 0, 1106, 0, 544, 109, -4, 2105, 1, 0, 109, 5, 1207, -3, 1, 10, 1006, 10, 567, 2207, -4, -2, 10, 1006, 10, 567, 22101, 0, -4, -4, 1106, 0, 635, 21202, -4, 1, 1, 21201, -3, -1, 2, 21202, -2, 2, 3, 21102, 586, 1, 0, 1105, 1, 544, 22101, 0, 1, -4, 21102, 1, 1, -1, 2207, -4, -2, 10, 1006, 10, 605, 21102, 0, 1, -1, 22202, -2, -1, -2, 2107, 0, -3, 10, 1006, 10, 627, 22101, 0, -1, 1, 21102, 1, 627, 0, 106, 0, 502, 21202, -2, -1, -2, 22201, -4, -2, -4, 109, -5, 2105, 1, 0]


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

def intcode(dataset, pointer, rbase, inputval):
  outindex = 0
  lastmove = False
  outval = [0, 0]
  relativebase = rbase

  opcode = get_opcode(dataset[pointer])
  opmode = get_opmode(dataset[pointer])

#  print(dataset, pointer, rbase, inputval)
#  print("relativebase : ", relativebase)
#  print()
  while opcode != 99:
    # Opcode 1 adds together numbers read from two positions and stores the result in a third position.
    if opcode == 1:
      #print("opcode : ",opcode," add       opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2],dataset[pointer+3])
      val1 = get_value(dataset, pointer, opmode, 2, relativebase)
      val2 = get_value(dataset, pointer, opmode, 1, relativebase)
      index3 = get_index(dataset, pointer, opmode, 0, relativebase)
      dataset[index3] = val1 + val2
      pointer += 4
  
    # Opcode 1 multiply together numbers read from two positions and stores the result in a third position.
    elif opcode == 2:
      #print("opcode : ",opcode," multiply  opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2],dataset[pointer+3])
      val1 = get_value(dataset, pointer, opmode, 2, relativebase)
      val2 = get_value(dataset, pointer, opmode, 1, relativebase)
      index3 = get_index(dataset, pointer, opmode, 0, relativebase)
      dataset[index3] = val1 * val2
      pointer += 4

    # Opcode 3 takes a single integer as input and saves it to the position given by its only parameter.
    elif opcode == 3:
      #print("opcode : ",opcode," input     opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1])
      #inval = input("Enter your value: ")
      inval = inputval
      index1 = get_index(dataset, pointer, opmode, 2, relativebase)
      dataset[index1] = int(inval)
      pointer += 2

    # Opcode 4 outputs the value of its only parameter.
    elif opcode == 4:
      #print("opcode : ", opcode, " output    opmode : ", opmode, " raw : ", dataset[pointer], dataset[pointer + 1])
      index1 = get_index(dataset, pointer, opmode, 2, relativebase)
      outval[outindex] = dataset[index1]
      outindex += 1
      #print("outval : ",outval)
      pointer += 2
      if outindex == 2:
        break

    #Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    elif opcode == 5:
      #print("opcode : ",opcode," jumptrue  opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2])
      val1 = get_value(dataset, pointer, opmode, 2, relativebase)
      val2 = get_value(dataset, pointer, opmode, 1, relativebase)
      if val1 != 0:
        pointer = val2
      else:
        pointer += 3
    
    #Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    elif opcode == 6:
      #print("opcode : ",opcode," jumpfalse opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2])
      val1 = get_value(dataset, pointer, opmode, 2, relativebase)
      val2 = get_value(dataset, pointer, opmode, 1, relativebase)
      if val1 == 0:
        pointer = val2
      else:
        pointer += 3
    
    #Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    elif opcode == 7:
      #print("opcode : ",opcode," lessthan  opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2],dataset[pointer+3])
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
      #print("opcode : ",opcode," equals    opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2],dataset[pointer+3])
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
      #print("opcode : ",opcode," offset    opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1])
      val1 = get_value(dataset, pointer, opmode, 2, relativebase)
      relativebase += val1
      pointer += 2

    else:
      print("error opcode : ",opcode)
  
    opcode = get_opcode(dataset[pointer])
    opmode = get_opmode(dataset[pointer])
  
  if opcode == 99:
    lastmove = True
  
  return outval[0], outval[1], dataset, pointer, relativebase, lastmove

def move_robot(dataset, pointer, relativebase, coordinate, direction):
  #inputval is color
  inputval = coordinate[2]

  # robot brain
  result = intcode(dataset, pointer, relativebase, inputval)
  color = result[0]
  newdirection = turn(direction, result[1])
  dataset = result[2]
  pointer = result[3]
  relativebase = result[4]
  lastmove = result[5]

  if newdirection == "U":
    newcoordinate = (coordinate[0], coordinate[1] + 1)
  elif newdirection == "D":
    newcoordinate = (coordinate[0], coordinate[1] - 1)
  elif newdirection == "R":
    newcoordinate = (coordinate[0] + 1, coordinate[1])
  else:
    newcoordinate = (coordinate[0] - 1, coordinate[1])

  return dataset, pointer, relativebase, newcoordinate, color, newdirection, lastmove

def turn(orig, new):
  if orig == "U":
    if new == 0:
      direction = "L"
    else:
      direction = "R"
  elif orig == "D":
    if new == 0:
      direction = "R"
    else:
      direction = "L"
  elif orig == "R":
    if new == 0:
      direction = "U"
    else:
      direction = "D"
  elif orig == "L":
    if new == 0:
      direction = "D"
    else:
      direction = "U"
  else:
    print("orig direction error : ", orig)
  return direction

def get_color(coordinate_list, coord):
  x = coord[0]
  y = coord[1]
  color = 0
  for i in range(0, len(coordinate_list)):
    ii = len(coordinate_list) - i -1
    if coordinate_list[ii][0] == x and coordinate_list[ii][1] == y:
      color = coordinate_list[ii][2]
      break
  return color

## MAIN
# extend dataset memory
for i in range(0, 2000):
  dataset.append(0)

# coordinate is (x,y,color)
coordinate_list = [(0, 0, 1)]
lastmove = False
direction = "U"
coordinate = coordinate_list[0]
pointer = 0
relativebase = 0

# robot move
while not lastmove:
  origin = coordinate
  result = move_robot(dataset, pointer, relativebase, coordinate, direction)
  dataset = result[0]
  pointer = result[1]
  relativebase = result[2]
  coord = result[3]
  color = result[4]
  direction = result[5]
  lastmove = result[6]

  # update color on origin
  coordinate_list[-1] = ((origin[0], origin[1], color))

  # save new coordinate
  # get last color on coordinate
  lastcolor = get_color(coordinate_list, coord)
  coordinate = (coord[0], coord[1], lastcolor)
  coordinate_list.append(coordinate)

#  print(coordinate_list)
#  sleep(1)

# Final

# create coordinate list without color
coord_list = [(x[0], x[1]) for x in coordinate_list]

#filter uniq coordinate
uniq_coord_list = set(coord_list)
# total coordinate FYI
#print(len(uniq_coord_list))

# to draw letter, we need to know limits of painting
xmin = min(uniq_coord_list,key=lambda item:item[0])[0]
ymin = min(uniq_coord_list,key=lambda item:item[1])[1]
xmax = max(uniq_coord_list,key=lambda item:item[0])[0]+1
ymax = max(uniq_coord_list,key=lambda item:item[1])[1]+1
#print("xmin : ", xmin, "ymin : ", ymin, "xmax : ", xmax, "ymax : ", ymax)
total_lines = abs(ymin) + abs(ymax)
total_col = abs(xmin) + abs(xmax)
#print(total_lines,total_col)

#initialize drawing
drawing = []
for line in range(0, total_lines):
  line = []
  for char in range(0, total_col):
    line.append(' ')
  drawing.append(line)

for coord in uniq_coord_list:
  color = get_color(coordinate_list, coord)
  if color == 0:
    drawing[abs(coord[1])][abs(coord[0])] = ' '
  else:
    drawing[abs(coord[1])][abs(coord[0])] = '#'


#draw
for line in range(0, total_lines):
  newline = ''
  for char in range(0, total_col):
    newline = newline + drawing[line][char]
  print(newline)



#
#for i in uniq_coord_list:
#  color = get_color(coordinate_list, i)
#  draw(i,color)
#
#
#print(uniq_coord_list)