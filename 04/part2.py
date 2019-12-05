#!/usr/bin/env python
# encoding: utf-8

#    It is a six-digit number.
#    The value is within the range given in your puzzle input.
#    Two adjacent digits are the same (like 22 in 122345).
#    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
#    the two adjacent matching digits are not part of a larger group of matching digits.

passrange = ( 264793, 803935)

potential_password_list = []
for candidate in range(passrange[0],passrange[1]+1):

  # rule 1
  if len(str(candidate)) == 6:

    # rule 3+5
    double_list = []
    for i in range(0,len(str(candidate))-1):
      if str(candidate)[i] == str(candidate)[i+1]:
        double_list.append(str(candidate)[i])

    double_list_reduced=set(double_list)
    pure_double=0
    if len(double_list_reduced) > 0:
      for i in double_list_reduced:
        if str(candidate).find(str(i)+str(i)) >=0 and not(str(candidate).find(str(i)+str(i)+str(i)) >=0):
          pure_double=pure_double+1

    if pure_double >= 1:
      # rule 4
      rule4_flag=1
      for j in range(0,len(str(candidate))-1):
        if int(str(candidate)[j]) > int(str(candidate)[j+1]):
          rule4_flag=0
      if rule4_flag == 1:
        potential_password_list.append(candidate)

print(len(set(potential_password_list)))
