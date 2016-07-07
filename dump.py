from canard import can
from canard.hw import socketcan

dev = socketcan.SocketCanDev("vcan0")

dev.start()
while True:
    print(dev.recv())