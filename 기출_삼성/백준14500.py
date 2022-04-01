from collections import deque
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
paper=[]
max_val=0
for i in range(N):
    arr=list(map(int,input().split()))
    max_val=max(max_val,max(arr))
    paper.append(arr)

dx=[1,-1,0,0]
dy=[0,0,1,-1]
answer=0
def dfs(x,y,idx,total):
    global answer
    # 지금까지 구한 최댓값 answer이 지금까지 더한 값 total 에 최댓값을 남은 idx 만큼 더한 것보다 크거나 같으면 더이상 순회할 필요 없음
    if answer>=total +max_val*(3-idx):
        return
    if idx==3:
        answer=max(answer,total)
        return


    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<N and 0<=ny<M and visited[nx][ny]==-1:
            if idx==1:
                visited[nx][ny]=1
                dfs(x,y,idx+1,total+paper[nx][ny])
                visited[nx][ny]=-1

            visited[nx][ny] = 1
            dfs(nx, ny, idx + 1, total+paper[nx][ny])
            visited[nx][ny] = -1




visited=[[-1 for i in range(M)] for j in range(N)]

for i in range(N):
    for j in range(M):
        visited[i][j]=1
        dfs(i,j,0,paper[i][j])
        visited[i][j]=-1
print(answer)

