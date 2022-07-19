#백준 골드 5
# 백준 선수과목
import sys
input = sys.stdin.readline
N,K = map(int, input().split())
subject=[]
for i in range(K):
    first,last=map(int, input().split())
    subject.append((first,last))

subject.sort(reverse=False,key=lambda x:x[0])
dp=[1 for i in range(0,N+1)]

for i , j in subject:
    dp[j]=max(dp[i]+1,dp[j])


print(' '.join(str(s) for s in dp[1:]))
