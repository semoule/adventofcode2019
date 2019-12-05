#!/usr/bin/env python
# encoding: utf-8

#    It is a six-digit number.
#    The value is within the range given in your puzzle input.
#    Two adjacent digits are the same (like 22 in 122345).
#    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

passrange = ( 264793, 803935)

potential_password_list = []
for candidate in range(passrange[0],passrange[1]+1):
  # rule 1
  if len(str(candidate)) == 6:
    # rule 3
    rule3_flag=0
    for i in range(0,len(str(candidate))-1):
      if str(candidate)[i] == str(candidate)[i+1]:
        rule3_flag=1
      if rule3_flag == 1:
        # rule 4
        rule4_flag=1
        for j in range(0,len(str(candidate))-1):
          if int(str(candidate)[j]) > int(str(candidate)[j+1]):
            rule4_flag=0
        if rule4_flag == 1:
          potential_password_list.append(candidate)

print(len(set(potential_password_list)))