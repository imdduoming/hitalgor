import sys
limit_number = 10**5
sys.setrecursionlimit(limit_number)
N,K=map(int,input().split())
from collections import deque
queue=deque()
visited=[False for i in range(0,100001)]
queue.append((N,0))
graph=[(sys.maxsize,sys.maxsize) for i in range(0,100001)]
visited[N]=True

def path(x,answer):
    arr = []
    temp = x
    for _ in range(answer+1):
        arr.append(temp)
        temp = graph[temp]
    print(' '.join(map(str, arr[::-1])))

if N==K:
    print(0)
    print(N)
else:
    while queue:
        now,dist=queue.popleft()
        next1=now+1
        next2=now-1
        next3=now*2
        # print('now',now)
        # print('next1',next1)
        # print('next2',next2)
        # print('next3',next3)
        if 0<=next1<=100000 and visited[next1]==False:
            queue.append((next1,dist+1))
            graph[next1]=now
            visited[next1]=True
            if next1==K:
                answer=dist+1
                break
        if 0<=next2<=100000 and visited[next2]==False:
            queue.append((next2,dist+1))
            graph[next2]=now
            visited[next2]=True
            if next2==K:
                answer=dist+1
                break
        if 0<=next3<=100000 and visited[next3]==False:
            queue.append((next3,dist+1))
            graph[next3]=now
            visited[next3]=True
            if next3==K:
                answer=dist+1
                break
    print(answer)
    path(K,answer)

