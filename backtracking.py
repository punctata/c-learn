n = 4
counter = 0
col = [False] * n
diag1 = [False] * (2*n-1)
diag2 = [False] * (2*n-1)

def search(y):
    global counter
    if y == n:
        counter += 1
    else:
        for x in range(n):
            if col[x] or diag1[x+y] or diag2[x-y+n-1]: continue
            col[x] = diag1[x+y] = diag2[x-y+n-1] = True
            search(y+1)
            col[x] = diag1[x+y] = diag2[x-y+n-1] = False

search(0)
print counter