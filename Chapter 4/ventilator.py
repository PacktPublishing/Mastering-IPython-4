import zmq
import random
import time

context = zmq.Context()

# socket to send messages on
sender = context.socket(zmq.PUSH)
sender.bind("tcp://localhost:5555")

while True:
    # messages come in batches of 16, for this example
    # perhaps there are 16 workers
    for i in range(16):
        seed = random.randint(1, 20000)
        sender.send_string(str(seed))

    # give 0MQ time to deliver and workers time to work
    time.sleep(10)

