#특정거리의 도시찾기
#실버2
from collections import deque
import sys
input=sys.stdin.readline
N,M,K,X=map(int,input().split())

graph=[[] for i in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)

queue=deque()
queue.append(X)

dist=[-1 for i in range(N+1)]
dist[X]=0
while queue:
    now=queue.popleft()
    for i in graph[now]:
        if dist[i]==-1:
            dist[i]=dist[now]+1
            queue.append(i)

result = []
for i in range(1,N+1):
    if dist[i]==K:
        result.append(i)
result.sort()

if result:
    for i in result:
        print(i)
else:
    print(-1)