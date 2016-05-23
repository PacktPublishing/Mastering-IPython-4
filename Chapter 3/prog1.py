import queue
import threading

def f(n, q):
    curr = n
    tmp = 1
    while curr != 1:
        tmp = tmp + 1
        if curr % 2 == 1:
            curr = 3 * curr + 1
        else:
            curr = curr/2
    q.put(tmp)

def main( ):
    sum = 0
    q = Queue.Queue()
    threads = []

    for i in range(100):
        t = threading.Thread(target=f, args=(i+1, q))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        threads[i].join()

    while (not q.empty()):
        sum = sum + q.get()

    avg = sum / 100.0
    print(“avg = “, avg)

