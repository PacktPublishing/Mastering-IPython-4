import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, “weather”)

while True:
    wtr = socket.recv_string()
    print(“the weather is: “ + wtr)

