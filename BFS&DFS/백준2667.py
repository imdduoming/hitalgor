from collections import deque
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(graph,x,y):
    queue=deque()
    queue.append((x,y))
    graph[x][y]=0
    cnt=1

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            next_x=x+dx[i]
            next_y=y+dy[i]
            if 0<=next_x and next_x<n and 0<=next_y and next_y<n:
                if graph[next_x][next_y] == 1:
                    cnt += 1
                    graph[next_x][next_y] = 0
                    queue.append((next_x,next_y))

    return cnt


answer=[]
for i in range(0,n):
    for j in range(0,n):
        if graph[i][j]==1:
            answer.append(bfs(graph,i,j))

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])