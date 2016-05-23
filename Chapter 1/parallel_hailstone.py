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
    procs = getProcs(100)
    i = 1

    for proc in procs:
        proc.setFun(f, i)
        i = i + 1

    for proc in procs:
        sum = sum + proc.execute( )

    avg = sum / 100.0

