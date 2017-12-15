from curses import wrapper
from status import Status
from motor import Motor
import curses
from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()
    window = curses.initscr()
    window.nodelay(1)
    window.keypad(True)

    WaitTime = 1/float(3000)
    leftMotor = Motor("Left", [23,24,25,26], WaitTime)
    rightMotor = Motor("Right", [18,19,20,21], WaitTime)
    while True:
        ch = window.getch()
        stdscr.addstr(0, 0, 'Testing the print option {} here {}'.format(ch, 2000))
        if ch==curses.KEY_UP: #up
          leftMotor.StepDir= 1
          rightMotor.StepDir =1
        if ch==curses.KEY_DOWN: #down
          leftMotor.StepDir= -1
          rightMotor.StepDir = -1
        if ch==curses.KEY_LEFT: #left
          leftMotor.StepDir= -1
          rightMotor.StepDir = 1
        if ch==curses.KEY_RIGHT: #right
          leftMotor.StepDir= 1
          rightMotor.StepDir = -1
        if ch==27:
          window.endwin()
          break
        leftMotor.update()
        rightMotor.update()

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)