import sys
input=sys.stdin.readline
N=int(input())
stair=[]
for i in range(N):
    stair.append(int(input()))
dp=[0 for i in range(N)]

for i in range(0,N):
    if i==0:
        dp[0] = stair[0]
    elif i==1:
        dp[1] = stair[0] + stair[1]
    elif i==2:
        dp[2]=max(stair[0]+stair[2],stair[1]+stair[2])

    else:

        case1=stair[i]+stair[i-1]+dp[i-3]
        case2=stair[i]+dp[i-2]

        dp[i]=max(case1,case2)


print(dp.pop())