
n = 3
arr = [0, 5, 9]

subset = []
def search(k):
    if k == n:
        print subset
    else:
        search(k + 1)
        subset.append(arr[k])
        search(k + 1)
        del subset[-1]

search(0)

import itertools

print list(itertools.permutations([1,3,9]))