#백준 점프점프
#실버2
import sys
input = sys.stdin.readline
N=int(input())
miro=list(map(int,input().split()))

dp=[100]*(N)
dp[0]=0

for i in range(0,N):
    for j in range(1,miro[i]+1):
        if i+j>=N:
            break
        dp[i+j]=min(dp[i+j],dp[i]+1)

if dp[N-1]==100:
    print(-1)

else:
    print(dp[N-1])