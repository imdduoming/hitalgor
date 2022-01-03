#백준13459
# 백준 골드3
from collections import deque
n = int(map(input().split()))
graph = []
for i in range(n):
    graph.append(list(map(input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(x,y,bx,by,n,graph):
    fail=0
    queue=deque()
    queue.append((x,y,bx,by,'first'))
    cnt=0
    while queue:
        x,y,bx,by,direct=queue.popleft()
        if graph[x][y]=='O':
            if x==bx or y==by:
                fail=1
            break


        for i in range(4):
            next_x=x+dx[i]
            next_y=y+dy[i]
            if 1 <= next_x < n-1 and  1 <= next_y < n-1:
                if graph[next_x][next_y]=='.' :
                    if i==0: #오른쪽
                        next_direct='right'
                        next_bx=bx
                        next_by=by+1
                        if 1 <= next_bx < n -1 and 1 <= next_by < n - 1 :
                            if graph[next_bx][next_by]!='.':
                                next_by=y


                    elif i==1: #왼쪽
                        next_direct = 'left'
                        next_bx = bx
                        next_by = by - 1
                        if 1 <= next_bx < n - 1 and 1 <= next_by < n - 1:
                            if graph[next_bx][next_by] != '.':
                                next_by = y
                    elif i==2: #위쪽
                        next_direct = 'up'

                        next_bx = bx + 1
                        next_by = by
                        if 1 <= next_bx < n - 1 and 1 <= next_by < n - 1:
                            if graph[next_bx][next_by] != '.':
                                next_by = y
                    else: #아래쪽
                        next_direct = 'down'

                        next_bx = bx - 1
                        next_by = by
                        if 1 <= next_bx < n - 1 and 1 <= next_by < n - 1:
                            if graph[next_bx][next_by] != '.':
                                next_by = y

                    if direct!=next_direct: #방향바뀌면 횟수증가
                        cnt+=1
                    queue.append((next_x,next_y,next_bx,next_by,next_direct))

    if cnt>10:
        return 0
    else:
        return 1


for i in range(n):
    for j in range(n):
        if graph[i][j]=='B':
            bx=i
            by=j
            break

for i in range(n):
    for j in range(n):
        if graph[i][j]=='R':
            dfs(i,j,bx,by,graph,n)
