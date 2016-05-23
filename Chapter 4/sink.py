import zmq

context = zmq.Context()

# socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://localhost:5556")

while True:
    s = receiver.recv_string()
    # do work – maybe log time for each completed process

