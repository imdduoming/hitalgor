N,M,K = map(int,input().split())
arr=[[0 for i in range(M+1)]for j in range(N+1)]
for i in range(K):
    a,b=map(int,input().split())
    arr[a][b]=1
from collections import deque
def bfs(arr,x,y,visited):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=1
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    cnt=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            next_x=x+dx[i]
            next_y=y+dy[i]
            if 0<=next_x <=N and 0<=next_y <=M:
                if arr[next_x][next_y] == 1 and visited[next_x][next_y]==-1:
                    cnt += 1
                    queue.append((next_x,next_y))
                    visited[next_x][next_y]=1

    return visited, cnt
max_junk=0
visited=[[-1 for i in range(M+1)]for j in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        if arr[i][j]==1 and visited[i][j]==-1:
            visited,junk=bfs(arr,i,j,visited)
            max_junk=max(max_junk,junk)

print(max_junk)