#!/usr/bin/python

from status import Status
from motor import Motor
import curses

window = curses.initscr()
window.nodelay(1)

WaitTime = 1/float(3000)
leftMotor = Motor("Left", [23,24,25,26], WaitTime)
rightMotor = Motor("Right", [18,19,20,21], WaitTime)
while True:
   ch = window.getch()
   if ch==27:
      leftMotor.StepDir= -1*leftMotor.StepDir
   if ch==1:
       break
   leftMotor.update()
   rightMotor.update()


leftMotor.displayStatus()
leftMotor.displayStatus()
