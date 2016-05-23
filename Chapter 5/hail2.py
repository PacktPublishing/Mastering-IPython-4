import time
import random

def f(n):
    curr = n
    tmp = 0
    time.sleep(random.random())
    while curr != 1:
        tmp = tmp + 1
        if curr % 2 == 1:
            curr = 3 * curr + 1
        else:
            curr = curr/2
    return tmp
