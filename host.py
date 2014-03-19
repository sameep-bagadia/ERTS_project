import serial 
import time
from socketIO_client import SocketIO

import logging
logging.basicConfig(level=logging.DEBUG)

ser = serial.Serial('/dev/tty.usbserial-AH001BS6')
x = ser.read(3)
print x

"""
In each iteration:
-> read button press from bot
-> process video to find positions
-> read directions from remote
-> pass directions to firebird
-> send position and button press info to remote
"""

# to be done by pranav
def process_video():
    return "pos"

# to be implemented
def read_remote():
    return "dummy"

# to be implemented
def write_remote(str):
    return

def on_directions(*args):
    print "Hello host"
    print 'on_directions', args

print "rblah"
SERVER_IP = 'https://10.129.26.35'
socketH = SocketIO(SERVER_IP, 8080, verify=False)
socketB = SocketIO(SERVER_IP, 8080, verify=False)
print "rt"
socketH.emit('create or join', 'h0')
socketB.emit('create or join', 'b0')

# socketH.on('dir_response', on_directions)
socketB.on('dir_response', on_directions)

while True:
    button_pressed = ser.read(1)
    # print button_pressed
    if (button_pressed == "1"):
        print "Button pressed\n"
        # socketIO.emit('
        socketB.emit('message', {'type': 'ping', 'bot': 'b0'})
    
    
##    positions = process_video()
##    direction = read_remote()
##    ser.write(direction)
##    write_remote(button_pressed)
##    write_remote(positions)
##    
ser.close()

