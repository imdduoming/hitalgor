#백준 실버2
#DFS와 BFS
import sys
from collections import deque
input=sys.stdin.readline
N,M,V=map(int,input().split())
graph=[[] for i in range(N+1)]
for i in range(M):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(1,N+1):
    graph[i].sort()
def bfs(start):
    answer=[]
    queue=deque()
    queue.append(start)
    answer.append(start)

    visited = [-1 for j in range(N+1)]
    visited[start]=1
    while queue:
        start=queue.popleft()
        for i in graph[start]:
            if visited[i]==-1:
                queue.append(i)
                visited[i]=1
                answer.append(i)


    return answer
def dfs(start,visited_dfs,answer):
    answer.append(start)
    visited_dfs[start] = 1
    for i in graph[start]:

        if visited_dfs[i]==-1:
            dfs(i,visited_dfs,answer)
    return answer

answer1=bfs(V)
visited_dfs= [-1 for j in range(N+1)]
answer=[]
answer2=dfs(V,visited_dfs,answer)
for i in answer2:
    print(i,end=' ')
print()
for i in answer1:
    print(i, end=' ')
