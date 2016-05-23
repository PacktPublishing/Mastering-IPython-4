import zmq
import random
import time

context = zmq.Context()

# from the ventilator
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5555")

# to the sink
sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5556")

while True:
    s = receiver.recv()

    #do some “work”
    time.sleep(int(s)*0.001)

    #send “results” to sink
    tm = str(time.time())
    sender.send_string(tm)

