from multiprocessing import Pool

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

if __name__ == '__main__':
    pool = Pool(processes=4)

    x = pool.apply(f, (1109,))
    print(type(x))
    print(x)

    x = pool.apply_async(f, (1109, ))
    print(type(x))
    print(x.get())

    x = pool.map(f, range(1100, 1110))
    print(type(x))
    print(x)

    x = pool.map_async(f, range(1100, 1110))
    print(type(x))
    print(x.get( ))

    x = pool.imap(f, range(1100, 1110))
    print(type(x))
    for i in x:
        print(i)

    x = pool.imap_unordered(f, range(1100, 1110))
    print(type(x))
    for i in x:
        print(i)

