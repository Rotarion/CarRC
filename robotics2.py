import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
from evdev import InputDevice, categorize, ecodes

left_neg = 7
left_pos = 11
right_neg = 15
right_pos = 13

btnForward = 307
btnReverse = 304
btnLeft = 306
btnRight = 305
btnPivotLeft = 310
btnPivotRight = 311


gamepad = InputDevice("/dev/input/event1")

bDebug = True

def DbgPrint(str):
    global bDebug
    if bDebug:
        print(str)

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    
def stop():
    init()
    DbgPrint("Stop")
    gpio.output(left_neg, False)
    gpio.output(left_pos, False)
    gpio.output(right_pos, False)
    gpio.output(right_neg, False)
    gpio.cleanup()

def forward(tf):
    init()
    DbgPrint("Forward")
    gpio.output(left_neg, False)
    gpio.output(left_pos, True)
    gpio.output(right_pos, True)
    gpio.output(right_neg, False)
    #time.sleep(tf)
    gpio.cleanup()


def reverse(tf):
    init()
    DbgPrint("Reverse")
    gpio.output(left_neg, True)
    gpio.output(left_pos, False)
    gpio.output(right_pos, False)
    gpio.output(right_neg, True)
    #time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    init()
    DbgPrint("Right")
    gpio.output(left_neg, False)
    gpio.output(left_pos,False)
    gpio.output(right_pos, True)
    gpio.output(right_neg, False)
    #time.sleep(tf)
    gpio.cleanup()

def turn_left(tf):
    init()
    DbgPrint("Left")
    gpio.output(left_neg, False)
    gpio.output(left_pos, True)
    gpio.output(right_pos, False)
    gpio.output(right_neg, False)
    #time.sleep(tf)
    gpio.cleanup()

def pivot_right(tf):
    init()
    DbgPrint("Pivot Right")
    gpio.output(left_neg, True)
    gpio.output(left_pos, False)
    gpio.output(right_pos, True)
    gpio.output(right_neg, False)
    #time.sleep(tf)
    gpio.cleanup()

def pivot_left(tf):
    init()
    DbgPrint("Pivot Left")
    gpio.output(left_neg, False)
    gpio.output(left_pos, True)
    gpio.output(right_pos, False)
    gpio.output(right_neg, True)
    #time.sleep(tf)
    gpio.cleanup()



def key_input(event):
    print 'Key:', event.char
    key_press = event.char
    sleep_time = 0.030
    
    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        reverse(sleep_time)
    elif key_press.lower() == 'a':
        turn_left(sleep_time)
    elif key_press.lower() == 'd':
        turn_right(sleep_time)
    elif key_press.lower() == 'q':
        pivot_left(sleep_time)
    elif key_press.lower() == 'e':
        pivot_right(sleep_time)

def handle_input(btnIn, value):
    sleep_time = 0.01
    if not value:
        stop()
    else:
        if btnIn == btnForward:
            forward(sleep_time)
        elif btnIn == btnReverse:
            reverse(sleep_time)
        elif btnIn == btnLeft:
            turn_left(sleep_time)
        elif btnIn == btnRight:
            turn_right(sleep_time)
        elif btnIn == btnPivotLeft:
            pivot_left(sleep_time)
        elif btnIn == btnPivotRight:
            pivot_right(sleep_time)
    

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        #btnIn = event.code
        handle_input(event.code, event.value)
    #        print(event)
    
#command = tk.Tk()
#command.bind('<KeyPress>', key_input)
#command.mainloop()
