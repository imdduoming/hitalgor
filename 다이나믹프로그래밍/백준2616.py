#백준 2616
#백준 소형기관차 골드4
import sys
input=sys.stdin.readline
N=int(input())
guests=list(map(int,input().split()))
guests=[0]+guests
k=int(input())
dp = [[0] * (N + 1) for _ in range(4)]
total=[0]

for i in range(1,N+1):
    total.append(total[i - 1] + guests[i])


for i in range(1, 4):
    for j in range(k, N + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - k] + total[j] - total[j - k])

print(dp[3][N])