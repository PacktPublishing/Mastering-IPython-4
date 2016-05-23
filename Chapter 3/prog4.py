def monteCarloPI(n):
    s = 0
    for i in xrange(n):
        x = random()
        y = random()
        if x*x + y*y <= 1:
            s+=1
    return 4.*s/n
    
def parCalcPI(view, n):
    p = len(view.targets)
    
    ar = view.apply(monteCarloPI, n)
    return sum(ar)/p

