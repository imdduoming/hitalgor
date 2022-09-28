import heapq  # 우선순위 큐 구현을 위함
from collections import deque
import sys

input = sys.stdin.readline
T=int(input())
for i in range(T):
    N,K = map(int,input().split())
    time=list(map(int,input().split()))
    time = [0]+time

    visit = [False] * (N+1)
    inDegree = [0] * (N+1)
    dp = [0] * (N+1)
    tree= [[] for a in range(N+1)]
    for j in range(K):
        # 규칙
        start, end = map(int,input().split())
        tree[start].append(end)
        inDegree[end]+=1
    queue=deque()
    for k in range(1,N+1):
        if inDegree[k]==0:
            queue.append(k)
            dp[k]=time[k]
    while queue:
        now=queue.popleft()
        for a in tree[now]:
            inDegree[a]-=1
            dp[a]=max(dp[now]+time[a],dp[a])
            if inDegree[a]==0:
                # 이 차례가 되면
                queue.append(a)
    arrive=int(input().rstrip())
    print(dp[arrive])


