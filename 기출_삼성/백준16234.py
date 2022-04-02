#인구이동
#골드5
import sys
from collections import deque
input=sys.stdin.readline
N,L,R=map(int,input().split())
space=[]
search_list=[]
for i in range(N):
    arr=list(map(int,input().split()))
    space.append(arr)
    search_list += [(i, j) for j in range(N)]
search_list = deque(search_list)
def bfs(x,y,visited):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    total = space[x][y]
    queue=deque()
    queue.append((x,y))
    unit=set([(x,y)])
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==-1:
                if L<=abs(space[nx][ny]-space[x][y])<=R:
                    visited[nx][ny] = 1
                    total+= space[nx][ny]
                    unit.add((nx,ny))
                    queue.append((nx,ny))


    if len(unit)>1:
        new_pop = total // len(unit)
        for x, y in unit:
            space[x][y] = new_pop
            search_list.append((x,y))
        return True
    else:
        return False


answer=0
while search_list:
    visited = [[-1 for j in range(N)] for i in range(N)]
    Flag=False
    for _ in range(0,len(search_list)):
        i,j=search_list.popleft()
        if visited[i][j]==-1:
            visited[i][j]=1
            if bfs(i,j,visited):
                Flag=True

    if Flag==False:
        break
    else:
        answer+=1

print(answer)