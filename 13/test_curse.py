#!/usr/bin/env python
# encoding: utf-8

import curses

screen = curses.initscr()
screen.addstr("Hello World!!!")
screen.refresh()
screen.getch()
curses.endwin()