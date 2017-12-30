import random
import copy

a = 


n = 2000000
print n
x = [None] * n
for i in xrange(n):
    x[i] = random.randint(0, 100000000)
print " ".join(map(str, x))
