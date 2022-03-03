#백준 알파벳
import sys
input=sys.stdin.readline
R,C=map(int,input().split())

array=[list(map(lambda x:ord(x)-65,input().rstrip())) for _ in range(R)]

visited=[-1 for j in range(26)]

answer=1
def dfs(x,y,cnt):

    global answer
    global visited
    visited[array[x][y]]=1

    answer=max(answer,cnt)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<R and 0<=ny<C and  visited[array[nx][ny]]==-1:
            dfs(nx,ny,cnt+1)
            visited[array[nx][ny]]=-1


    return answer

print(dfs(0,0,1))





