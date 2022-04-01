#인구이동
#골드5
import sys
from collections import deque
input=sys.stdin.readline
N,L,R=map(int,input().split())
space=[]
for i in range(N):
    arr=list(map(int,input().split()))
    space.append(arr)

def bfs(x,y,visited):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    total = space[x][y]
    queue=deque()
    queue.append((x,y))
    unit=[]
    unit.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==-1:
                if L<=abs(space[nx][ny]-space[x][y])<=R:
                    visited[nx][ny] = 1
                    total+= space[nx][ny]
                    unit.append((nx,ny))
                    queue.append((nx,ny))

    new_pop=total//len(unit)
    for x,y in unit:
        space[x][y]=new_pop
    print(space)
    if len(unit)>=2:
        return True
    else:
        return False


answer=0
while True:
    visited = [[-1 for j in range(N)] for i in range(N)]
    Flag=False
    for i in range(0,N):
        for j in range(0,N):
            if visited[i][j]==-1:
                if bfs(i,j,visited):
                    Flag=True

    if Flag==False:
        break
    else:
        answer+=1
        print(answer)

print(answer)