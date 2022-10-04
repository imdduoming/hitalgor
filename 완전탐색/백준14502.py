#세울수있는 벽의 위치
def go_virus(i,j,visited,maps):
    from collections import deque
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue=deque([])
    queue.append((i,j))
    visited[i][j]=True
    while queue:
        x,y=queue.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<N and 0<=ny<M and maps[nx][ny]!=1 and visited[nx][ny]==False:
                queue.append((nx,ny))
                visited[nx][ny]=True
                maps[nx][ny]=2
    return visited,maps

def get_safe(walls,org_maps,N,M):
    from copy import deepcopy
    maps=deepcopy(org_maps)
    visited=[[False for i in range(M)]for j in range(N)]
    for wall in walls:
        maps[wall[0]][wall[1]]=1

    real_total=0
    for i in range(N):
        for j in range(M):
            if maps[i][j]==2 and visited[i][j]==False:
                visited,maps = go_virus(i,j,visited,maps)


    for i in range(N):
        for j in range(M):
            if maps[i][j]==0:
                real_total +=1

    # print('case 최종',real_total)
    return real_total


from itertools import combinations
N,M = map(int,input().split())
maps =[]
for i in range(N):
    arr= list(map(int,input().split()))
    maps.append(arr)
viruses=[]
walls=[]
for i in range(N):
    for j in range(M):
        if maps[i][j]==2:
            viruses.append((i,j))
        elif maps[i][j]==0:
            walls.append((i,j))

max_val=0
for i in set(combinations(walls,3)):
    max_val=max(get_safe(i,maps,N,M),max_val)

print(max_val)