# 백준 14499
# 백준 주사위 굴리기
# 주사위 모양 바뀜
def change_dice(dir,dice):
    if dir==1:
        dice[1],dice[2],dice[3],dice[5]=dice[5],dice[1],dice[2],dice[3]
    elif dir==2:
        dice[1],dice[2],dice[3],dice[5]=dice[2],dice[3],dice[5],dice[1]
    elif dir==3: #북
        dice[0],dice[2],dice[4],dice[5]=dice[2],dice[4],dice[5],dice[0]
    else: #남
        dice[0],dice[2],dice[4],dice[5]=dice[5],dice[0],dice[2],dice[4]

    return dice

def dice_move(x,y,dir,dice,map):
    dx=[0,0,-1,1]
    dy= [1,-1,0,0]
    nx = x+dx[dir-1]
    ny=y+dy[dir-1]
    move_flag=False
    # print('nx',nx,'ny',ny)
    if 0<=nx<N and 0<=ny<M:
        move_flag=True
        # 주사위 이동하고 밑면 비교
        dice = change_dice(dir,dice)
        # print('이동 후 dice',dice)
        if map[nx][ny]==0:
            map[nx][ny]=dice[-1]
        else:
            dice[-1]=map[nx][ny]
            map[nx][ny]=0
        # print('최종 dice',dice)
        # print('map',map)
        return nx,ny,dice,map,move_flag
    else:
        return x,y,dice,map,move_flag


N,M,x,y,K =map(int,input().split())
maps= []

for i in range(N):
    arr = list(map(int, input().split()))
    maps.append(arr)
command = list(map(int, input().split()))
dice=[0,0,0,0,0,0]
for comm in command:
    x,y,dice,maps,flag=dice_move(x,y,comm,dice,maps)
    if flag==True:
        print(dice[2])
