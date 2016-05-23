def countWords(filename):
    int numWords = 0
    f = open(filename, “r”)
    for line in f:
        words = line.split( )
        numWords += len(words)
    return numWords

c = Client()
numEngines = 4
dv = c[:]
asyncResults = []

for i in range(numFiles):
    filename = “infile” + i + “.txt”
    dv.targets = i % numEngines]
    asyncResults.append(dv.apply(countWords, fileName))

for r in asyncResults:
    results.append(r.get())

