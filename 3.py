def solution(n, edges):
    answer = 0
    graph=[[0 for j in range(n+1)] for i in range(n+1)]
    dist=[[-1 for i in range(n+1)] for j in range(n+1)]
    from collections import deque
    queue=deque()

    def bfs(start):
        queue.append(start)
        while queue:
            now = queue.popleft()
            for i in graph[now]:
                if dist[now][i] == -1:
                    dist[i] = dist[now] + 1
                    queue.append(i)

    for i in range(n):
        bfs(i)
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if graph[a][b] == (graph[a][k] + graph[k][b])

    return answer