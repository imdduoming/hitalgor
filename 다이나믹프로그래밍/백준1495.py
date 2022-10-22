N,S,M= map(int,input().split())
arr = list(map(int,input().split()))
dp=[[0 for _ in range(M+1)] for _ in range(N+1)]
dp[0][S]=1
for i in range(1,N+1):
    for j in range(0,M+1):
        if dp[i-1][j]==0:
            continue
        if j-arr[i-1]>=0:
            dp[i][j-arr[i-1]]=1
        if j+arr[i-1]<=M:
            dp[i][j+arr[i-1]]=1
answer=-1
for i in range(0,M+1):
    if dp[N][i]==1:
        answer=i
print(answer)