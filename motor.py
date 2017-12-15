import sys
import time
import RPi.GPIO as GPIO
from status import Status

class Motor:
   def __init__(self, name, StepPins, waitTime):
      GPIO.setwarnings(False)
      GPIO.setmode(GPIO.BCM)
      self.name = name
      self.StepPins = StepPins
      self.waitTime = waitTime
      self.status = Status.STATIONED
      self.StepDir = 1      
      self.StepCounter = 0
      self.Seq = [[1,0,0,1],
                [1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1]]
      
      for pin in self.StepPins:
         GPIO.setup(pin,GPIO.OUT)
         GPIO.output(pin, False)
      

   def displayStatus(self):
      print("Name : ", self.name,  ", Wait Time: ", self.waitTime,  ", status: ", self.status)
      print(self.status == Status.STATIONED);

   def update(self):
      StepCount = len(self.Seq)
      for pin in range(0, 4):
         xpin = self.StepPins[pin]
         if self.Seq[self.StepCounter][pin]!=0:
           
            GPIO.output(xpin, True)
         else:
            GPIO.output(xpin, False)

      self.StepCounter += self.StepDir

      # If we reach the end of the sequence
      # start again
      if (self.StepCounter>=StepCount):
         self.StepCounter = 0
      if (self.StepCounter<0):
         self.StepCounter = StepCount+self.StepDir

      # Wait before moving on
      time.sleep(self.waitTime)