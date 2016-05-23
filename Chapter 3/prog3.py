def gpuWrap(dv, q):
    q.add(dv.apply(useGPUs))
    
def fWrap(dv, i, q):    
    q.add(dv.apply(f, i))


# we assume that the engines have been correctly instantiated
def main( ):
    q = Queue.Queue() # collect results in here
    threads = []
    seqNum = 1

    c = Client()
        
    for i in range(100):
        dv = c[i]
        if i % 4 == 0:
            # we assume the GPU is attached to processing element 0
            t = threading.Thread(target=gpuWrap, args=(dv, q))
        else:
            t = threading.Thread(target=fWrap, args=(dv, seqNum, q))
            seqNum = seqNum + 1

        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        threads[i].join()

# at this point q should be full of AsyncResult objects that can be used to
# get the results of the individual processes as they complete

