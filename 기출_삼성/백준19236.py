import copy
from collections import deque
space=[]
for i in range(4):
    arr=list(map(int,input().split()))
    new_arr=[]
    for j in range(0,7,2):
        new_arr.append([arr[j],arr[j+1]])
        if arr[j]==1:
            start_x=i
    space.append(new_arr)
for i in range(0,4):
    if space[start_x][i][0]==1:
        start_y=i

dx=[0,-1,-1,0,1,1,1,0,-1]
dy=[0,0,-1,-1,-1,0,1,1,1]

dead_fish={}
dead_fish[space[0][0][0]]=1
shark_dir=space[0][0][1]
shark_x=0
shark_y=0
# 물고기 위치 찾는 함수
def find_fish(new_space,num):
    for i in range(0,4):
        for j in range(0,4):
            if new_space[i][j][0]==num:
                return i,j
    return -1,-1

def swap_fish(new_space,x,y,nx,ny):
    temp_x,temp_y=new_space[x][y][0],new_space[x][y][1]
    new_space[x][y][0]=new_space[nx][ny][0]
    new_space[x][y][1]=new_space[nx][ny][1]
    new_space[nx][ny][0], new_space[nx][ny][1]=temp_x,temp_y

def move_fish(new_space,dead_fish,shark_x,shark_y):
    #1번부터 16번째 물고기까지 움직이기
    for i in range(1, 17):
        #물고기 죽었다면 조회안함
        if i in dead_fish and dead_fish[i]==1:
            continue
        # 현재물고기의 방향과 위치
        x,y=find_fish(new_space,i)
        dir=new_space[x][y][1]
        # 이동할 위치
        nx=x+dx[dir]
        ny=y+dy[dir]
        #범위를 벗어나지않고 다음 범위에 상어가 있는 위치가 아니라면
        new_dir = dir
        while True:
            if 0<=nx<4 and 0<=ny<4 and not (shark_x==nx and shark_y==ny):
                #바뀐 방향으로 갱신
                new_space[x][y][1]=new_dir
                swap_fish(new_space,x,y,nx,ny)
                break

            #반시계 방향으로 회전
            if new_dir==8:
                nx = x + dx[((new_dir + 1) % 9)+1]
                ny = y + dy[((new_dir + 1) % 9)+1]
                new_dir = ((new_dir + 1) % 9) + 1
            else:
                nx= x+ dx[((new_dir+1)%9)]
                ny = y + dy[((new_dir+1)%9)]
                new_dir=((new_dir+1)%9)

    return new_space

#상어가 먹을 수 있는 물고기 리스트
def eat_fish_list(shark_x ,shark_y,shark_dir,new_space):
    nx=shark_x
    ny=shark_y
    candidate=[]
    while True:
        nx=nx+dx[shark_dir]
        ny=ny+dy[shark_dir]
        if 0>nx or nx>3 or ny<0 or ny>3:
            break
        # 물고기가 없는 칸으로는 이동할 수 없다.
        if new_space[nx][ny][0]!=-1:
            candidate.append((nx,ny))
    return candidate

ans=0
#상어 움직이는 함수
def move_shark(dead_fish,space,shark_x ,shark_y,shark_dir,total):
    global ans
    new_space=copy.deepcopy(space)
    dead_fish_copy=copy.deepcopy(dead_fish)
    new_space=move_fish(new_space,dead_fish_copy,shark_x,shark_y)
    # print('현재 상어 위치',shark_x,shark_y)
    fish_candidate=eat_fish_list(shark_x ,shark_y,shark_dir,new_space)
     #후보 찾음
    # print('후보뽑고 new space',new_space)
    # print('먹이후보',fish_candidate)
    for i,j in fish_candidate:
        #물고기 잡아먹힘
        fish= new_space[i][j][0]
        shark_dir=new_space[i][j][1]
        new_space[i][j][0] = -1
        new_space[i][j][1] = -1
        dead_fish_copy[fish]=1
        # print('잡아먹힌 물고기',fish,shark_dir)
        # print('dead_fish',dead_fish_copy)
        # print(new_space)
        move_shark(dead_fish_copy,new_space,i, j, shark_dir,total+fish)
        dead_fish_copy[fish] = 0
        new_space[i][j][0] = fish
        new_space[i][j][1] = shark_dir

    ans=max(ans,total)


total=space[0][0][0]
space[0][0][0]=-1
space[0][0][1]=-1

move_shark(dead_fish,space,shark_x ,shark_y,shark_dir,total)
print(ans)