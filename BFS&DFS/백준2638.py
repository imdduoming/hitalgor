#백준 골드 4 치즈
#BFS
import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
cheese=[]
for i in range(N):
    row=list(map(int,input().split()))
    cheese.append(row)



def bfs():
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    visited=[[-1 for i in range(M)]for j in range(N)]
    queue=deque()
    queue.append((0,0))

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            next_x=x+dx[i]
            next_y=y+dy[i]

            if 0<=next_x<N and 0<=next_y<M and visited[next_x][next_y]==-1:
                #공기일경우
                if cheese[next_x][next_y]==0:
                    visited[next_x][next_y]=1
                    queue.append((next_x,next_y))
                #치즈일 경우 , 치즈와 접한 횟수 +!
                else:
                    cheese[next_x][next_y]+=1


    return cheese

time=0
while True:
    total=0
    time += 1
    cheese=bfs()

    for i in range(N):
        for j in range(M):
            if cheese[i][j]>=3:
                cheese[i][j]=0
            elif cheese[i][j]==2:
                cheese[i][j]=1
        total+=sum(cheese[i])

    if total==0:
        break


print(time)