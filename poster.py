from socketIO_client import SocketIO
import logging
logging.basicConfig(level=logging.DEBUG)

def on_directions(*args):
    print "Hello host"
    print 'on_directions', args

SERVER_IP = 'https://10.129.26.35'
socketH = SocketIO(SERVER_IP, 8080, verify=False)
socketH.on('dir', on_directions)

socketH.wait(seconds=100)

