import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    msg = socket.recv()
    timeStr = str(time.time())
    socket.send(timeStr)

