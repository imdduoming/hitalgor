from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
schedule=[]
for i in range(N):
    time,money=map(int,input().split())
    schedule.append((time,money))

ans=0
def dfs(day,money):
    global ans
    if day>N:
        return
    if day==N:
        ans = max(ans, money)
        return
    ans=max(ans,money)
    dfs(day+1,money)
    dfs(day+schedule[day][0],money+schedule[day][1])

dfs(0,0)
print(ans)