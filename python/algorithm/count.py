def counts_if(vector, func=None, icount=0):
    for v in vector:
        if func(v):
            icount += 1