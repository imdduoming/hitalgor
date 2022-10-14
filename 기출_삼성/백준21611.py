def init_info(space):
    cnt=N**2-1
    loc=(0,-1)
    dir=0
    dist=N
    change_dir=1
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    num_dict={}
    loc_dict={}
    ball_cnt =[0 for i in range(cnt+1)]
    while True:
        for i in range(dist):
            nx=loc[0]+dx[dir]
            ny=loc[1]+dy[dir]
            loc_dict[(nx,ny)]=cnt #좌표 -> 번호
            num_dict[cnt]=(nx,ny) # 번호 -> 좌표
            ball_cnt[cnt]=space[nx][ny] # 번호 -> 구슬 갯수
            # 좌표 갱신
            loc = (nx,ny)
            cnt-=1

        dir=(dir+1)%4
        change_dir+=1
        if change_dir==2:
            dist-=1
            change_dir=0

        if cnt==0:
            break

    return ball_cnt , loc_dict , num_dict

def move_ball(ball_cnt,cnt): #구슬정리
    # cnt 는 N**2

    new_ball_cnt =[0]
    for i in range(1,len(ball_cnt)):
        if ball_cnt[i]!=-1:
            new_ball_cnt.append(ball_cnt[i])
    if len(new_ball_cnt) < cnt :
        need_cnt = cnt - len(new_ball_cnt)
        new_ball_cnt += [0] * need_cnt

    return new_ball_cnt

def throw_ice(dir,dist,sx,sy,ball_cnt): #얼음던지기
    x=sx
    y=sy
    dx =[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(dist):
        nx =x+dx[dir]
        ny =y+dy[dir]
        num_ball = loc_dict[(nx,ny)] # 좌표 번호 찾기
        ball_cnt[num_ball] = -1 # 구슬 0개
        x,y=nx,ny
    return ball_cnt

def ball_pop(pops,cnt,ball_cnt): #구슬 폭발

    while True: #폭발하는 구슬 없을 때 까지
        destroy = False
        for i in range(1,cnt-1):
            target= ball_cnt[i]

            if target == -1 or target==0:
                continue
            else:
                # print('비교 대상',target)
                serial =False
                balls =[i]
                for j in range(i+1,cnt):
                    if target!=ball_cnt[j]: #연속하지 않으면
                        break
                    else: #연속하는 경우
                        serial=True
                        balls.append(j)
                if serial ==True: #연속
                    if len(balls)>=4: #연속하는 구슬이 4개 이상일 때 폭발
                        for ball in balls:
                            ball_cnt[ball]=-1
                        pops[target]+=len(balls)
                        destroy =True
                        ball_cnt = move_ball(ball_cnt,cnt)


        if destroy ==False: # 다 돌아도 폭발하지 않았다면
            break

    return pops , ball_cnt

def make_group(ball_cnt,leng):
    new_ball=[0] # 상어의미 0
    end = False
    for i in range(1,len(ball_cnt)):
        target = ball_cnt[i]
        ball_cnt[i]=-1
        cnt , group_num = 1, target
        if target!=-1 and target!=0: #처음 방문
            if i!=(len(ball_cnt)-1):
                for j in range(i+1,len(ball_cnt)):
                    if target==ball_cnt[j]:
                        ball_cnt[j]=-1
                        cnt+=1
                    else:
                        break

            new_ball.append(cnt)
            new_ball.append(target)
            if len(new_ball) == (N**2):
                end = True
                break

    if end ==False:

        need = leng-len(new_ball)
        new_ball += [0]*need

    return new_ball



N,M= map(int,input().split())
space =[]
for i in range(N):
    arr = list(map(int,input().split()))
    space.append(arr)
command=[]
for i in range(M):
    dir ,dist = map(int,input().split())
    command.append((dir,dist))
ball_cnt, loc_dict , num_dict = init_info(space)

sx,sy= (N-1)//2 , (N-1)//2
pops=[0,0,0,0]
for comm in command:
    dir , dist = comm[0] , comm[1]
    # 구슬파괴
    ball_cnt=throw_ice(dir-1,dist,sx,sy,ball_cnt)
    # 구슬 정리
    ball_cnt=move_ball(ball_cnt,N**2)
    pops,ball_cnt = ball_pop(pops,N**2,ball_cnt)
    ball_cnt= make_group(ball_cnt,N**2)

total=0
for i in range(1,4):
    total+= pops[i]*i
print(total)


