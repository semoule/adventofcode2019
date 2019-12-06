#!/usr/bin/env python
# encoding: utf-8

import sys

## DATA
filepath = "./06.txt"

## FUNCTIONS
# orbital parental chain
def get_chain(object,orbital_list):
  older_parent_found = False
  parental_chain = [object]
  child = object

  while not older_parent_found:
    object_parent = None

    for orbital in orbital_list:
      if orbital[1] == child:
        object_parent = orbital[0]
        parental_chain.append(object_parent)

    if object_parent == None:
      older_parent_found = True
   
    else:
      child = object_parent

  return parental_chain

# occurence of object in parental chain list
def orbital_count(object, orbital_chain_list):
  sum = 0
  for chain in orbital_chain_list:
    sum = sum + chain.count(object)
  return sum



## MAIN
# create tuple list of orbital
orbital_list = []
with open(filepath) as fp:
  line = fp.readline()
  while line:
    orbital_value = line.strip().split(')')
    orbital_list.append((orbital_value[0],orbital_value[1]))
    line = fp.readline()

# create orbital object list
orbital_object_list= []
for object in orbital_list:
  orbital_object_list.append(object[0])
  orbital_object_list.append(object[1])
orbital_object_list = set(orbital_object_list)

# for each orbital object create orbital chain
orbital_chain_list = []
for object in orbital_object_list:
  orbital_chain_list.append(get_chain(object,orbital_list))

# total orbital count
sum = 0
for object in orbital_object_list:
  if object != "COM":
    sum = sum + orbital_count(object,orbital_chain_list)

print(sum)
