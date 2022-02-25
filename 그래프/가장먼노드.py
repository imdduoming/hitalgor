from collections import deque

def solution(n, edge):
    answer = 0
    graph=[[] for j in range(n+1)]
    for i,j in edge:
        graph[i].append(j)
        graph[j].append(i)
    visited=bfs(n,1,graph)
    max_val=max(visited)
    for i in visited:
        if i==max_val:
            answer+=1


    return answer

def bfs(n,start,graph):
    queue=deque()
    queue.append((start,0))
    visited = [0 for i in range(n + 1)]
    visited[start]=1
    while queue:
        now,cost=queue.popleft()
        for i in graph[now]:
            if visited[i]==0:
                visited[i]=cost+1
                queue.append((i,cost+1))



    return visited
print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))