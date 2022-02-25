#프로그래머스 게임맵최단거리 (level2)
from collections import deque
def solution(maps):

    x_len=len(maps)

    y_len=len(maps[0])

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    maps[0][0]=0
    queue=deque()
    queue.append((0,0,1))
    while queue:
        x,y,answer=queue.popleft()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < x_len and 0 <= next_y < y_len:
                  if maps[next_x][next_y] == 1:
                    maps[next_x][next_y] = answer+1
                    queue.append((next_x,next_y,maps[next_x][next_y]))

    if maps[x_len-1][y_len-1]==1:
        return -1
    else:
        return maps[x_len-1][y_len-1]
