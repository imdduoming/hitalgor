import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int, input().split())
miro=[]
for i in range(N):
    row=list(map(int, input().split()))
    miro.append(row)

dp=[[0 for i in range(M+1)] for j in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j]=max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+miro[i-1][j-1]
print(dp[N][M])