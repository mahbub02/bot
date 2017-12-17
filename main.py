from curses import wrapper
from status import Status
from motor import Motor
import thread
import time

WaitTime = 1/float(3000)
leftMotor = Motor("Left", [23,24,25,26], WaitTime)
rightMotor = Motor("Right", [18,19,20,21], WaitTime)

def takeInput(threadName, extradiarakhlam):
    while 1:
        ch = raw_input("L/R/F/B/S ?")
        if ch=='f': #forward
          leftMotor.StepDir= 1
          rightMotor.StepDir =1
        if ch=='b': #back
          leftMotor.StepDir= -1
          rightMotor.StepDir = -1
        if ch=='l': #left
          leftMotor.StepDir= -1
          rightMotor.StepDir = 1
        if ch=='r': #right
          leftMotor.StepDir= 1
          rightMotor.StepDir = -1
        if ch=='s':
          exit()

try:
    thread.start_new_thread( takeInput, ("Thread-1", 2, ) )
    #thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
    print "Error: unable to start thread"

while 1:
    leftMotor.update()
    rightMotor.update()
    pass
    

