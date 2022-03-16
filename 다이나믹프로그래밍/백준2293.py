#동전1
#골드5
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))
dp=[[0 for i in range(k+1)] for j in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        if i==1:
            if j%arr[i-1]==0:
                dp[i][j]=1
            else:
                dp[i][j]=0
        elif arr[i-1]==j:
            dp[i][j] = dp[i][j - arr[i - 1]] + dp[i - 1][j]+1
        else:

            dp[i][j] = dp[i][j - arr[i - 1]] + dp[i-1][j]

print(dp[n][k])