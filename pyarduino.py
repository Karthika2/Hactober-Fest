#Python Code for Running arduino

import serial
import time

ArduinoSerial = serial.Serial('com4',baudrate=9600, timeout=2)
time.sleep(2)

def led_on():
    arduinoData.write('1')


def led_off():
    arduinoData.write('0')




"""
while 1:
    ArduinoSerial.write(b'1')
    print('ON')
    time.sleep(1)
    ArduinoSerial.write(b'0')
    print('OFF')
    time.sleep(1)
"""


while 1: #Do this forever
   data = ArduinoSerial.readline().decode('ascii')
   print(data)
"""
    var = input() #get input from user
    print("you entered", var) #print the intput for confirmation
    
    if (var == '1'): #if the value is 1
        ArduinoSerial.write('HI') #send 1
        print ("LED turned ON")
        time.sleep(1)
    
    if (var == '0'): #if the value is 0
        ArduinoSerial.write('NO') #send 0
        print ("LED turned OFF")
        time.sleep(1)
"""
