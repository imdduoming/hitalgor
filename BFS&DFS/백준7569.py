#백준 파이썬
import sys
from collections import deque
input = sys.stdin.readline
M,N,H = map(int, input().split())
boxes=[]
for i in range(H):
    box=[]
    for j in range(N):
        row= list(map(int, input().split()))
        box.append(row)
    boxes.append(box)

def bfs(queue):
    while queue:
        h,x,y,cnt=queue.popleft()
        visited[h][x][y] = 1
        for i in range(6):
            nh=h+dh[i]
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nh<H and 0<=nx<N and 0<=ny<M:
                if visited[nh][nx][ny]==-1 and boxes[nh][nx][ny]==0:
                    boxes[nh][nx][ny]=cnt+1
                    queue.append((nh,nx,ny,cnt+1))


dh=[1,-1,0,0,0,0]
dx=[0,0,1,-1,0,0]
dy=[0,0,0,0,1,-1]


visited=[[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]

queue=deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k]==1:
                queue.append((i,j,k,1))

bfs(queue)
max_val=0
answer=1
for i in range(H):
    for j in range(N):
        for k in range(M):
            #익지 않는 토마토 있는 경우
            if  boxes[i][j][k]==0:
                answer=-1
                break
            max_val=max(max_val, boxes[i][j][k])
        if answer==-1:
            break
    if answer == -1:
        break

if answer==1:
    print(max_val-1)

else:
    print(-1)