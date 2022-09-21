# 백준 이모티콘
# 백준 골드 4
from collections import deque
S= int(input())
def command(i,now,clip):
    if i==0:
        #클립보드에 복사
        clip=now
    elif i==1:
        # 복
            now+=clip
    else:
            now-=1
    return now,clip
def bfs():
    queue=deque([])
    queue.append((1,0,0))
    visited=[[-1 for i in range(S+1)]for j in range(S+1)]
    visited[1][0]=1
    while queue:
        now,clip,cnt =queue.popleft()
        if now==S:
            return cnt
        for i in range(3):
            new_now,new_clip = command(i,now,clip)
            if S>=new_now>=0 and S>=new_clip>=0 and visited[new_now][new_clip]==-1:
                # print('case',i,'화면',new_now,'클',new_clip,cnt)
                    visited[new_now][new_clip]=1
                    queue.append((new_now,new_clip,cnt+1))

print(bfs())