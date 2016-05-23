import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

while True:
    msg = socket.recv()
    socket.send(“peanut butter jelly time”)

