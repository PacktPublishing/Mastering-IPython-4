from ipyparallel import Client
import os

c = Client( )
dv = c[:]

def f(n):
    from time import sleep
    import random
    curr = n
    tmp = 0
    while curr != 1:
        sleep(random.random( )/1000)
        tmp = tmp + 1
        if curr % 2 == 1:
            curr = 3 * curr + 1
        else:
            curr = curr/2
    return tmp

x = dv.apply(f, 1109)
print(type(x))
results = x.get_dict( )
print("results = ", results)

x = dv.apply_async(f, 63728127)
print(type(x))
print("done yet? ", x.ready( ))
results = x.get( )
print("done now? ", x.ready())
print("results = ", results)

x = dv.map(f, range(1, 10))
print(type(x))
results = x.get_dict( )
print("results in dict = ", results)

x = dv.map(f, range(1, 10))
print(type(x))
results = x.get( )
print("results in list = ", results)

x = dv.map_async(f, range(1100, 1110))
print(type(x))
results = x.get( )
print("results = ", results)

lbv = c.load_balanced_view( )

x = lbv.map(f, range(1100, 1110))
print(type(x))
results = x.get( )
print("results = ", results)

