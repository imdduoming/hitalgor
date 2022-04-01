#백준 실버2
#백준 외판원순회
import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
route=[]
for i in range(N):
    arr=list(map(int,input().split()))
    route.append(arr)
answer=sys.maxsize
def find(start,now,idx,dist):
    global answer
    if idx==N-1:
        if route[now][start]==0:
            return
        dist=dist+route[now][start]
        answer=min(answer,dist)
        return

    for i in range(0,N):
        if visited[i]==-1 and route[now][i]!=0:
            visited[i]=1
            find(start,i,idx+1,dist+route[now][i])
            visited[i]=-1


for i in range(0,N):
    visited = [-1 for i in range(N)]
    visited[i]=1
    find(i,i,0,0)


print(answer)