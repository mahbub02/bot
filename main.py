
from status import Status
from motor import Motor
import thread
import time


from bluetooth import *
import os
import glob





WaitTime = 1/float(3000)
leftMotor = Motor("Left", [23,24,25,26], WaitTime)
rightMotor = Motor("Right", [18,19,20,21], WaitTime)

def motorResponse(ch):
    print "motor response to [%s]" % ch
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
      leftMotor.StepDir= 0
      rightMotor.StepDir = 0

def bluetoothInput(threadName, extradiarakhlam):
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    server_sock=BluetoothSocket( RFCOMM )
    server_sock.bind(("",PORT_ANY))
    server_sock.listen(1)
    port = server_sock.getsockname()[1]
    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    advertise_service( server_sock, "AquaPiServer",
                       service_id = uuid,
                       service_classes = [ uuid, SERIAL_PORT_CLASS ],
                       profiles = [ SERIAL_PORT_PROFILE ], 
    #                   protocols = [ OBEX_UUID ] 
                        )
    client_sock, client_info = server_sock.accept()
    while True:          
        print "Waiting for connection on RFCOMM channel %d" % port
        print "Accepted connection from ", client_info
        try:
            data = client_sock.recv(1024)
            if len(data) == 0: break
            print "received [%s]" % data
            motorResponse(data)
            #client_sock.send(data)
        except IOError:
            pass
        except KeyboardInterrupt:

            print "disconnected"

            client_sock.close()
            server_sock.close()
            print "all done"

            break



def takeInput(threadName, extradiarakhlam):
    while 1:
        ch = raw_input("L/R/F/B/S ?")
        motorResponse(ch)

try:
    thread.start_new_thread( takeInput, ("Thread-1", 2, ) )
    thread.start_new_thread( bluetoothInput, ("Thread-2", 4, ) )
except:
    print "Error: unable to start thread"

while 1:
    leftMotor.update()
    rightMotor.update()
    pass
    

