import serial 
import time
from socketIO_client import SocketIO

ser = serial.Serial(19)
#x = ser.read(3)
#print x

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
    # type directions
    print 'on_directions', args

print "rblah"
socketIO = SocketIO('10.129.28.16', 8080)
print "rt"
socketIO.on('message', on_directions)
# socketIO.wait(seconds=1)

while True:
    #button_pressed = ser.read(1)
    #if (button_pressed == "1"):
        # socketIO.emit('
    socketIO.emit('message', {'type': 'ping', 'bot': 'b0'})
    print "Button pressed\n"
    
##    positions = process_video()
##    direction = read_remote()
##    ser.write(direction)
##    write_remote(button_pressed)
##    write_remote(positions)
##    
ser.close()

