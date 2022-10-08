# 백준 1504
# 백준 특정한 최단경로
import sys
import heapq  # 우선순위 큐 구현을 위함

def dijkstra(graph, start):
    dp = [sys.maxsize for i in range(len(graph) + 1)]
    dp[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, [start, 0])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        now,now_dist = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.
        # print('now',now,'now_dist',now_dist)
        if now_dist > dp[now]:
            continue
        for new, new_dist in graph[now]:
            distance = now_dist + new_dist  # 해당 노드를 거쳐 갈 때 거리
            if distance < dp[new]:  # 알고 있는 거리 보다 작으면 갱신
                dp[new] = distance
                heapq.heappush(queue, [new,distance])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

    return dp
input= sys.stdin.readline
N, E = map(int, input().split())
graph =[[] for j in range(N+1)]
for i in range(E):
    start , end , dist = map(int, input().split())
    graph[start].append((end,dist))
    graph[end].append((start,dist))

v1,v2=map(int, input().split())
start_dist = dijkstra(graph,1)
v1_dist = dijkstra(graph,v1)
v2_dist =  dijkstra(graph,v2)

answer = min(start_dist[v1]+v1_dist[v2]+v2_dist[N],start_dist[v2]+v2_dist[v1]+v1_dist[N])
if answer < sys.maxsize:
    print(answer)
else:
    print(-1)