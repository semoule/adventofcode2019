#!/usr/bin/env python
# encoding: utf-8

import itertools

## DATA
dataset = [3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 38, 55, 64, 81, 106, 187, 268, 349, 430, 99999, 3, 9, 101, 2, 9, 9, 1002, 9, 2, 9, 101, 5, 9, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 101, 3, 9, 9, 1002, 9, 4, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 5, 9, 1001, 9, 4, 9, 102, 4, 9, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 1001, 9, 5, 9, 102, 3, 9, 9, 1001, 9, 4, 9, 102, 5, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 99]

#dataset = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]

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

def intcode(dataset,phase,inputsignal):
#  print(dataset)
  pointer = 0
  opcode = get_opcode(dataset[pointer])
  opmode = get_opmode(dataset[pointer])

  inputvalue = (phase, inputsignal)
  inputindex = 0

  while opcode != 99:
    if opcode == 1:
      #print("opcode : ",opcode," add       opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2],dataset[pointer+3])
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
      #print("opcode : ",opcode," multiply  opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2],dataset[pointer+3])
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
      #print("opcode : ",opcode," input     opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1])
      #inval = input("Enter your value: ")
      inval = inputvalue[inputindex]
      inputindex = inputindex + 1
      pos1 = int(dataset[pointer + 1])
      dataset[pos1] = int(inval)
      pointer = pointer + 2
  
    elif opcode == 4:
      #print("opcode : ",opcode," output    opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1])
      pos1 = int(dataset[pointer + 1])
      outval = dataset[pos1]
      #print(outval)
      pointer = pointer + 2
  
    #Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    elif opcode == 5:
      #print("opcode : ",opcode," jumptrue  opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2])
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
      #print("opcode : ",opcode," jumpfalse opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2])
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
      #print("opcode : ",opcode," lessthan  opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2],dataset[pointer+3])
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
      #print("opcode : ",opcode," equals    opmode : ",opmode," raw : ",dataset[pointer],dataset[pointer+1],dataset[pointer+2],dataset[pointer+3])
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
  
  return outval


## MAIN

# compute all possible amplifier combination
x = [0, 1, 2, 3, 4]
amplifier_combination_list = list(itertools.permutations(x, 5))
#print(amplifier_combination_list)

amplifier_chain_list = []
for combination in amplifier_combination_list:
  inputsignal = 0
  for i in combination:
    phase = i
    outputsignal = intcode(dataset, phase, inputsignal)
    inputsignal = outputsignal
  amplifier_chain_list.append(outputsignal)

print(max(amplifier_chain_list))
