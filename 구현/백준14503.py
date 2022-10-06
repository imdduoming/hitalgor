# 현재 위치를 청소한다.
# 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
# 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
# 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
# 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
# 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.

def find(x,y,d,maps):
    visited=[[False for i in range(M)]for j in range(N)]
    dx =[-1,0,1,0]
    dy= [0,1,0,-1]
    clean_cnt =0
    cnt=0
    while True:
        # print('현재위치',x,y)
        # print('현재방향',d)
        if 0<=x <N and 0<=y<M and maps[x][y] == 0 and visited[x][y]==False: # 청소
            visited[x][y]=True
            cnt=0
            clean_cnt+=1
            # print('청소')

        nd= (d+3) %4
        nx = x+dx[nd]
        ny=  y+dy[nd]
        # print('다음방향',nd)
        # print('순회위치',nx,ny)
        if 0<=nx <N and 0<=ny<M and maps[nx][ny] == 0 and visited[nx][ny]==False: # 청소 찾음
            x=nx
            y=ny
            d=nd
            # print('청소찾')
        else: #청소 못찾음
            # print('청소못찾')
            cnt+=1
            if cnt==4:
                #네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
                nx = x-dx[(nd)%4]
                ny = y-dy[(nd)%4]
                if 0<=nx<N and 0<=ny<M and maps[nx][ny]==0:
                    x=nx
                    y=ny
                    d=nd
                    cnt=0
                    # print('후진')
                else:
                    break
            else:
                d=nd
    return clean_cnt

N,M=map(int,input().split())
now_x,now_y,now_d = map(int,input().split())
maps =[]
for i in range(N):
    arr= list(map(int,input().split()))
    maps.append(arr)

print(find(now_x,now_y,now_d,maps))


# 8 10
# 0 0 0
# 0 1 1 1 0 1 0 0 0 1
# 0 0 0 0 0 1 0 0 0 1
# 0 1 0 0 1 0 1 0 0 0
# 1 1 1 0 1 1 1 0 0 1
# 1 0 1 1 0 1 0 0 0 1
# 1 0 0 0 0 1 1 0 0 0
# 0 0 0 1 1 1 0 1 0 1
# 0 1 1 1 1 0 1 0 0 0
# 12 9
# 0 0 0
# 0 0 0 1 1 0 0 0 1
# 0 0 1 0 0 0 0 1 1
# 1 0 1 0 0 0 0 0 1
# 1 0 0 0 1 1 0 1 1
# 0 0 1 1 1 0 0 0 1
# 0 1 1 1 1 0 1 0 1
# 1 0 1 1 1 0 0 1 1
# 0 0 0 0 1 0 0 1 1
# 1 0 0 0 0 0 0 1 1
# 1 0 1 1 0 1 1 1 0
# 1 1 0 1 1 1 0 1 0
# 1 0 1 1 1 1 1 0 0
# 6 6
# 2 1 3
# 1 1 1 1 1 1
# 1 0 0 0 0 1
# 1 0 1 1 1 1
# 1 0 1 1 1 1
# 1 0 1 1 1 1
# 1 1 1 1 1 1
# 출처: https://joey09.tistory.com/122 [joie de vivre:티스토리]