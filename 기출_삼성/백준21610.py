def cloud_move(dir,dist,cloud):
    new_cloud=[]
    dx=[0,-1,-1,-1,0,1,1,1]
    dy=[-1,-1,0,1,1,1,0,-1]
    while cloud:
        x,y = cloud.pop()
        nx= (x+(dx[dir]*dist))%N
        ny=(y+(dy[dir]*dist))%N
        new_cloud.append((nx,ny))
    return new_cloud

def rain(cloud,space):
    for i,j in cloud:
        space[i][j]+=1
    return space

def copy_water(cloud,space):
    dx=[-1,-1,1,1]
    dy=[-1,1,-1,1]
    for x,y in cloud:
        cnt=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if space[nx][ny]>0:
                    cnt+=1
        space[x][y]+=cnt
    return space

def make_cloud(space,cloud):
    # print('구름생성 전 cloud',cloud)
    cloud_arr=[[0 for i in range(N)] for j in range(N)]
    for i,j in cloud:
        cloud_arr[i][j]=1
    new=[]
    for i in range(N):
        for j in range(N):
            if space[i][j]>=2 and not cloud_arr[i][j]:
                new.append((i,j))
                space[i][j]-=2
    # print('구름생성 후 cloud',cloud_arr)
    return space, new

N,M =map(int,input().split())
space=[]
for i in range(N):
    arr = list(map(int,input().split()))
    space.append(arr)
cloud=[(N-1,0),(N-1,1),(N-2,0),(N-2,1)]

for i in range(M):
    dir ,dist = map(int,input().split())
    new_cloud = cloud_move(dir-1,dist,cloud)
    space = rain(new_cloud,space)
    space = copy_water(new_cloud,space)
    space , new = make_cloud(space,new_cloud)
    cloud= new
    # print('space',space)
total=0
for i in range(N):
    total+=sum(space[i])
print(total)