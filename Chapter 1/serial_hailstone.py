def f(n):
    curr = n
    tmp = 1
    while curr != 1:
        tmp = tmp + 1
        if curr % 2 == 1:
            curr = 3 * curr + 1
        else:
            curr = curr/2
    return tmp

def main( ):
    sum = 0
    for i in range(1, 101):
        sum = sum + f(i)
    avg = sum / 100.0
