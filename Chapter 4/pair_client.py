import zmq

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:5555" % port)

while True:
    socket.send("What time is it?")
    msg = socket.recv()
    print msg
    time.sleep(1)

