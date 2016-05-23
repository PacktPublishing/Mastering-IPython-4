import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

while True:
    topic = “time”
    messagedata = str(time.time())
    socket.send(topic + “ “ + messagedata)

    topic = “weather”
    messagedata = “dark and stormy night”
    socket.send(topic + “ “ + messagedata)

    time.sleep(1)

