x = "LOVE"
y = "MOVIE"
dp = [[0]*(len(y)+1) for _ in range(len(x)+1)]
#Initializing
dp[0] = range(len(y)+1)
for i in range(len(x)+1):
    dp[i][0] = i

def cost(i,j):
    if x[i-1] == y[j-1]: return 0
    else: return 1

for a in range(1,len(x)+1):
    for b in range(1,len(y)+1):
        dp[a][b] = min(min(dp[a-1][b]+1,dp[a][b-1]+1),dp[a-1][b-1]+cost(a,b))

for i in range(0, len(x) + 1):
    print " ".join(map(str, dp[i]))