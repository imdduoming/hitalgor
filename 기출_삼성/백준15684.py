import sys

input = sys.stdin.readline
from collections import deque

graph = []
N, M, H = map(int, input().split())
line=[[False for j in range(N+1)] for i in range(H+1)]
for i in range(M):
    a,b = map(int, input().split())
    line[a][b]=True

garos=[]
for i in range(1,H+1):
    for j in range(1,N):
        if line[i][j]==False and line[i][j-1]==False and line[i][j+1]==False:
            #가로선을 추가할 수 있는 상황 , 현재 세로선에 없고 양 왼 오른쪽에 가로선 없고 , 연속적이면 안되기 때문에
            garos.append((i,j))


def go():
    for i in range(1,N+1):
        #시작하는 세로선
        start=i
        for j in range(1,H+1):
            if line[j][start-1]:
                start-=1
            elif line[j][start]:
                start+=1
        #제대로 도착 못함
        if start!=i:
            return False
    return True


def dfs(cnt_garo,num):
    global ans
    if cnt_garo>=ans:
        return
    if go():
        ans=cnt_garo
        return

    for idx in range(num,len(garos)):
    #하나씩 추가하면서 사다리게임 가능한지 체크
        x,y=garos[idx]
        if line[x][y-1]==False and line[x][y+1]==False:
            line[x][y]=True
            dfs(cnt_garo+1,idx+1)
            line[x][y]=False
ans=4
dfs(0,0)
if ans<4:
    print(ans)
else:
    print(-1)