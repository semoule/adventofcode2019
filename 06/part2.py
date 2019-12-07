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

  parental_chain.reverse()
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

# compute orbital chains for YOU and SAN
orbital_chain_list_you = get_chain('YOU',orbital_list)
orbital_chain_list_san = get_chain('SAN',orbital_list)

# get common path length from origin to YOU and from origin to SAN
i = 0
while orbital_chain_list_you[i] == orbital_chain_list_san[i]:
  i = i + 1

# shortest orbital transfer YOU to SAN
total = len(orbital_chain_list_you) - i + len(orbital_chain_list_san) - i - 2
print(total)