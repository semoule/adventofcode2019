#!/usr/bin/env python
# encoding: utf-8

import itertools
from time import sleep 
from os import system, name
import curses, time

def joystick():
  outval = 0
  c = stdscr.getch()
  if c == -1:
    outval = 0
  elif c == 260:
    outval = -1
  elif c == 261:
    outval = 1
  return outval

def main(stdscr):
    # do not wait for input when calling getch
    stdscr.nodelay(1)
    while True:
        time.sleep(1)
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        if c == -1:
          outval = 0
        elif c == 260:
          outval = -1
        elif c == 261:
          outval = 1
        print(outval)

if __name__ == '__main__':
    curses.wrapper(main)