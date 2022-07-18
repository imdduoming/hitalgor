import sys
input=sys.stdin.readline
arr=[0]
N=int(input())
for i in range(N):
    arr.append(int(input()))
dp=[0 for i in range(N+1)]

for i in range(1,N+1):
    if N==1:
        dp[1]=arr[1]
    elif N==2:
        dp[2]=arr[1]+arr[2]
    else:
        dp[i]=max(dp[i-1],dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])
print(dp[N])
