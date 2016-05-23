import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555" % port)
socket.connect("tcp://localhost:5556" % port)

while True:
    socket.send("What time is it?")
    msg = socket.recv()
    print msg
    time.sleep(1)

