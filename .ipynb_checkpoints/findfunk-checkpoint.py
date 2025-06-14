import numpy as np
def funk(arr):
    le = len(arr)
    if le%2 == 0:
        raise ValueError("ka digga")
    coun = (np.unique(arr,return_counts=True))
    count = 0

    for e,i in enumerate(coun[1]):
        if i == 1:
            count = count + 1
            val = coun[0][e]
    if count == 1:
        return val
    else:
        return False
