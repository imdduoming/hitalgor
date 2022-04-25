#동전1
#골드5
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))
dp=[0 for i in range(k+1)]
dp[0]=1
for coin in arr:
    for j in range(coin,k+1):
        # coin 으로 j를 만들 수 있는 경우의 수는 j-
        cnt=dp[j-coin]
        dp[j]+=cnt
print(dp[k])