#!/usr/bin/env python
# encoding: utf-8

## DATA
dataset = [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1102, 16, 13, 225, 1001, 88, 68, 224, 101, -114, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 2, 224, 1, 223, 224, 223, 1101, 8, 76, 224, 101, -84, 224, 224, 4, 224, 102, 8, 223, 223, 101, 1, 224, 224, 1, 224, 223, 223, 1101, 63, 58, 225, 1102, 14, 56, 224, 101, -784, 224, 224, 4, 224, 102, 8, 223, 223, 101, 4, 224, 224, 1, 223, 224, 223, 1101, 29, 46, 225, 102, 60, 187, 224, 101, -2340, 224, 224, 4, 224, 102, 8, 223, 223, 101, 3, 224, 224, 1, 224, 223, 223, 1102, 60, 53, 225, 1101, 50, 52, 225, 2, 14, 218, 224, 101, -975, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 3, 224, 1, 223, 224, 223, 1002, 213, 79, 224, 101, -2291, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 2, 224, 1, 223, 224, 223, 1, 114, 117, 224, 101, -103, 224, 224, 4, 224, 1002, 223, 8, 223, 101, 4, 224, 224, 1, 224, 223, 223, 1101, 39, 47, 225, 101, 71, 61, 224, 101, -134, 224, 224, 4, 224, 102, 8, 223, 223, 101, 2, 224, 224, 1, 224, 223, 223, 1102, 29, 13, 225, 1102, 88, 75, 225, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227, 274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 1107, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 329, 1001, 223, 1, 223, 108, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 344, 101, 1, 223, 223, 1008, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 359, 1001, 223, 1, 223, 1107, 226, 677, 224, 102, 2, 223, 223, 1006, 224, 374, 1001, 223, 1, 223, 8, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 389, 101, 1, 223, 223, 8, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 404, 101, 1, 223, 223, 7, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 419, 101, 1, 223, 223, 7, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 434, 101, 1, 223, 223, 1108, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 449, 1001, 223, 1, 223, 108, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 464, 101, 1, 223, 223, 1108, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 479, 101, 1, 223, 223, 1007, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 494, 1001, 223, 1, 223, 107, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 509, 1001, 223, 1, 223, 1008, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 524, 1001, 223, 1, 223, 1007, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 539, 101, 1, 223, 223, 1108, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 554, 1001, 223, 1, 223, 1008, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 569, 101, 1, 223, 223, 1107, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 584, 1001, 223, 1, 223, 7, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 599, 101, 1, 223, 223, 108, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 614, 101, 1, 223, 223, 107, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 629, 1001, 223, 1, 223, 107, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 644, 101, 1, 223, 223, 1007, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 659, 101, 1, 223, 223, 8, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 674, 1001, 223, 1, 223, 4, 223, 99, 226]

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


## MAIN
print(dataset)
pointer = 0
opcode = get_opcode(dataset[pointer])
opmode = get_opmode(dataset[pointer])

while opcode != 99:
  if opcode == 1:
    print("opcode : ",opcode," add       opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2],dataset[pointer+3])
    if opmode[2] == "0":
      val1 = int(dataset[int(dataset[pointer + 1])])
    else:
      val1 = int(dataset[pointer + 1])
    if opmode[1] == "0":
      val2 = int(dataset[int(dataset[pointer + 2])])
    else:
      val2 = int(dataset[pointer + 2])
    dataset[int(dataset[pointer + 3])] = val1 + val2
    pointer = pointer + 4

  elif opcode == 2:
    print("opcode : ",opcode," multiply  opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2],dataset[pointer+3])
    if opmode[2] == "0":
      val1 = int(dataset[int(dataset[pointer + 1])])
    else:
      val1 = int(dataset[pointer + 1])
    if opmode[1] == "0":
      val2 = int(dataset[int(dataset[pointer + 2])])
    else:
      val2 = int(dataset[pointer + 2])
    dataset[int(dataset[pointer + 3])] = val1 * val2
    pointer = pointer + 4

  elif opcode == 3:
    print("opcode : ",opcode," input     opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1])
    inval = input("Enter your value: ")
    pos1 = int(dataset[pointer + 1])
    dataset[pos1] = int(inval)
    pointer = pointer + 2

  elif opcode == 4:
    print("opcode : ",opcode," output    opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1])
    pos1 = int(dataset[pointer + 1])
    outval = dataset[pos1]
    print(outval)
    pointer = pointer + 2

  #Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
  elif opcode == 5:
    print("opcode : ",opcode," jumptrue  opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2])
    if opmode[2] == "0":
      val1 = int(dataset[int(dataset[pointer + 1])])
    else:
      val1 = int(dataset[pointer + 1])
    if opmode[1] == "0":
      val2 = int(dataset[int(dataset[pointer + 2])])
    else:
      val2 = int(dataset[pointer + 2])
    if val1 != 0:
      pointer = val2
    else:
      pointer = pointer + 3
  
  #Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
  elif opcode == 6:
    print("opcode : ",opcode," jumpfalse opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2])
    if opmode[2] == "0":
      val1 = int(dataset[int(dataset[pointer + 1])])
    else:
      val1 = int(dataset[pointer + 1])
    if opmode[1] == "0":
      val2 = int(dataset[int(dataset[pointer + 2])])
    else:
      val2 = int(dataset[pointer + 2])
    if val1 == 0:
      pointer = val2
    else:
      pointer = pointer + 3
  
  #Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
  elif opcode == 7:
    print("opcode : ",opcode," lessthan  opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2],dataset[pointer+3])
    if opmode[2] == "0":
      val1 = int(dataset[int(dataset[pointer + 1])])
    else:
      val1 = int(dataset[pointer + 1])
    if opmode[1] == "0":
      val2 = int(dataset[int(dataset[pointer + 2])])
    else:
      val2 = int(dataset[pointer + 2])
    val3 = int(dataset[pointer + 3])
    if val1 < val2:
      dataset[val3] = 1
    else:
      dataset[val3] = 0
    pointer = pointer + 4

  #Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
  elif opcode == 8:
    print("opcode : ",opcode," equals    opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2],dataset[pointer+3])
    if opmode[2] == "0":
      val1 = int(dataset[int(dataset[pointer + 1])])
    else:
      val1 = int(dataset[pointer + 1])
    if opmode[1] == "0":
      val2 = int(dataset[int(dataset[pointer + 2])])
    else:
      val2 = int(dataset[pointer + 2])
    val3 = int(dataset[pointer + 3])
    if val1 == val2:
      dataset[val3] = 1
    else:
      dataset[val3] = 0
    pointer = pointer + 4

  else:
    print("error opcode : ",opcode)

  opcode = get_opcode(dataset[pointer])
  opmode = get_opmode(dataset[pointer])
