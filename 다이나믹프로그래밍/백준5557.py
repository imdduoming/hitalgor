#다이나믹프로그래밍
import sys
input=sys.stdin.readline
N=int(input())
nums=list(map(int,input().split()))
dp=[[0 for j in range(21)] for i in range(N)]
dp[0][nums[0]]=1
for i in range(1,N-1):

        for j in range(21):
            if dp[i-1][j]:

                plus=j+nums[i]
                minus=j-nums[i]
                if 0<=plus<=20:
                    dp[i][plus]+=dp[i-1][j]
                if 0<=minus<=20:
                    dp[i][minus]+=dp[i-1][j]

answer=0

print(dp[N-2][nums[N-1]])
