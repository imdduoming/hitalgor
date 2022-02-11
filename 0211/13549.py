from collections import deque
N,M=map(int,input().split())
queue=deque()
visited=[-1 for _ in range(100001)]
queue.append((N,0))
visited[N]=1
while queue:
    now_loc,now_sec=queue.popleft()
    if now_loc==M:
        print(now_sec)
        break
    if 0<=now_loc-1:
        if visited[now_loc-1]==-1:
            queue.append((now_loc-1,now_sec+1))
            visited[now_loc-1]=1
    if now_loc*2 <= 100000:
        if visited[now_loc * 2] == -1:
            queue.appendleft((now_loc * 2, now_sec))
            visited[now_loc * 2] = 1
    if now_loc+1 <=100000:
        if visited[now_loc +1] == -1:
            queue.append((now_loc+1,now_sec+1))
            visited[now_loc +1] = 1


