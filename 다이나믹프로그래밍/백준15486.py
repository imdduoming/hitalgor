import sys
input=sys.stdin.readline
N= int(input())
table=[]
table.append((0,0))
for i in range(N):
    time,profit = map(int,input().split())
    table.append((time,profit))
dp =[0 for i in range(N+2)]
for i in range(1,N+1):
    if (i+table[i][0]) <= (N+1):
        #이번타임에 일함
        dp[i+table[i][0]] = max(dp[i]+table[i][1],dp[i+table[i][0]])
        #이번에 일안함
    dp[i+1]=max(dp[i],dp[i+1])
print(dp[N+1])