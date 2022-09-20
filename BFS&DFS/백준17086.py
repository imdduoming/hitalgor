# 백준 아기상어2
#백준 실버 2
from collections import deque
N,M=map(int,input().split())
space=[]
for i in range(N):
    arr=list(map(int,input().split()))
    space.append(arr)
dx=[-1,-1,-1,0,1,1,1,0]
dy=[-1,0,1,1,1,0,-1,-1]
def find_dist(x,y,space):
    queue=deque([])
    queue.append((x,y,1))
    visited=[[0 for i in range(M)] for j in range(N)]
    visited[x][y]=1
    while queue:
        x,y,dist= queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0:
                if space[nx][ny]==0:
                    queue.append((nx,ny,dist+1))
                    visited[nx][ny]=1
                else:
                    return dist


max_dist=0
for i in range(N):
    for j in range(M):
        if space[i][j]==0:
            dist= find_dist(i,j,space)
            # print('i',i,'j',j)
            # print('dist',dist)
            max_dist=max(max_dist,dist)

print(max_dist)