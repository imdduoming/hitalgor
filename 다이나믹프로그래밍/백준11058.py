# 백준 골드 5 dP 크리보드
N=int(input())
dp = [0 for i in range(N+1)]
dp[1]=1
dp[2]=2
for i in range(3,N+1):
    dp[i]=dp[i-1]+1
    for j in range(i-3,-1,-1):
        dp[i]=max(dp[i],dp[j]*(i-j-1))
print(dp[N])