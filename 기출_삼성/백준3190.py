#백준 3190
# 백준 뱀
from collections import deque
n = int(input())
k= int(input()) # 사과 갯수
ground =[[0 for i in range(n)] for j in range(n)]

for i in range(k):
    row,col=map(int,input().split())
    ground[row-1][col-1]=1

l = int(input())
direction = {}
for i in range(l):
    sec,dir=input().split()
    if sec not in dir:
        direction[int(sec)]=dir

def change_direction(sec,dir):
    # 방향 바꾸는 함수
    if direction[sec]=='D':
        # 오른쪽으로 이동
        next_dir= (dir+1)%4
    else:
        next_dir= (dir-1)%4
    return next_dir

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans=0
def go(hx,hy,sec,dir):
    # 부딪힐 경우 끝
    global ans
    snake= deque()
    snake.append((hx,hy))
    while True:
        hx,hy= snake.pop() #머리
        # 움직일 머리의 위치
        if sec in direction:
            dir= change_direction(sec,dir)
            # print('현재초',sec,'방향',dir)
        n_hx=hx+dx[dir]
        n_hy=hy+dy[dir]
        if n_hx<0 or n_hx>=n or n_hy<0 or n_hy>=n or (n_hx,n_hy) in snake:
    # 머리나 꼬리가 벽에 닿거나 자신의 몸에 부딪히면
            ans=sec+1
            broken=True
            break
        if ground[n_hx][n_hy]==1: #사과있으면
            ground[n_hx][n_hy]=0
            snake.append((hx,hy))
            snake.append((n_hx,n_hy))

        else:
            snake.append((hx,hy))
            snake.append((n_hx,n_hy))
            snake.popleft()
        sec+=1
        # print('snake',snake)
        # print('현재 초',sec)

    if broken==True:
        return ans



go(0,0,0,0)
print(ans)