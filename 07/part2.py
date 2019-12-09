#!/usr/bin/env python
# encoding: utf-8

import itertools

## DATA
#dataset = [3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 38, 55, 64, 81, 106, 187, 268, 349, 430, 99999, 3, 9, 101, 2, 9, 9, 1002, 9, 2, 9, 101, 5, 9, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 101, 3, 9, 9, 1002, 9, 4, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 5, 9, 1001, 9, 4, 9, 102, 4, 9, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 1001, 9, 5, 9, 102, 3, 9, 9, 1001, 9, 4, 9, 102, 5, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 99]

dataset = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]
#dataset = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54, -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]


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
  outval = None
  pointer = 0
  opcode = get_opcode(dataset[pointer])
  opmode = get_opmode(dataset[pointer])

  if phase == None:
    inputindex = 1
  else:
    inputindex = 0

  inputvalue = (phase, inputsignal)

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
x = [5, 6, 7, 8, 9]
amplifier_combination_list = list(itertools.permutations(x, 5))

amplifier_chain_list = []
for combination in amplifier_combination_list:
  amplification_process = True
  output_last_amplifier = 0
  loopcount=0

  while(amplification_process):

    inputsignal = output_last_amplifier

    for i in combination:
      if loopcount != 0:
        phase = None
      else:
        phase = i
      outputsignal = intcode(dataset, phase, inputsignal)
      inputsignal = outputsignal

    if outputsignal != None:
      output_last_amplifier = outputsignal
    else:
      amplification_process = False

    loopcount = loopcount + 1
 
  amplifier_chain_list.append(output_last_amplifier)
  
print(max(amplifier_chain_list))
