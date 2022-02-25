import sys
from collections import deque
input=sys.stdin.readline
N,M,K=map(int,input().split())
maps=[]
for i in range(N):
    arr=list(map(int,input().split()))
    maps.append(arr)

dice=[[0,2,0],
      [4,1,3],
      [0,5,0],
      [0,6,0]]

def change_dice(direction):
    #동
    if direction==0:
        tmp=dice[3][1]
        dice[3][1] = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0]=tmp
    #남
    elif direction==1:
        tmp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = tmp
    #서
    elif direction == 2:
        tmp = dice[3][1]
        dice[3][1] = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = tmp
    #북
    else:
        tmp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = tmp

    return dice

# 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
# 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
# A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
# A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
# A = B인 경우 이동 방향에 변화는 없다.
#시계빵향으로 동남서북


# 주사위가 이동 방향으로 한 칸 굴러간다. 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
def move_dice(x,y,direction):
    move_direction=[(0, 1), (1, 0), (0, -1), (-1, 0)]
    nx,ny=x+move_direction[direction][0],y+move_direction[direction][1]
    if 0<=nx<=N-1 and 0<=ny<=M-1:
        # 이동방향에 칸이 있는 경우
        return [nx,ny,direction]
    else:
        # 이동방향에 칸이 없는 경우 -> 반대방향으로 방향 바꾸기
        direction=(direction+2)%4
        nx,ny=x+move_direction[direction][0],y+move_direction[direction][1]
        return [nx,ny,direction]

#연속해서 이동할 수 있는(maps[x][y]와 값이 같아야 이동 가능) 칸의 갯수
def bfs(x,y):
    move_direction= [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cnt=1
    visited=[[0]*M for i in range(N)]
    queue=deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        x,y=queue.popleft()
        for i,j in move_direction:
            nx,ny=x+i,y+j
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0 and maps[nx][ny]==maps[x][y]:
                visited[nx][ny] = 1
                queue.append((nx,ny))
                cnt+=1
    return cnt

x,y=0,0
direct=0
total=0
for i in range(K):
    # 주사위가 이동 방향으로 한 칸 굴러간다. 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
    x,y,direct=move_dice(x,y,direct)
    dice = change_dice(direct)
    # 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
    C = bfs(x, y)
    A,B=dice[3][1],maps[x][y]
    total+=(B*C)
    # 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
    # A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
    if A>B:
        direct=(direct+1)%4
    # A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
    elif A<B:
        direct=direct-1
        if direct==-1:
            direct=3
    # A = B인 경우 이동 방향에 변화는 없다.
    elif A==B:
        pass

print(total)