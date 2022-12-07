R,C=map(int,input().split())
space=[]
for i in range(R):
    arr=list(input())
    space.append(arr)
cnt=0

#고슴도치 위치 저장
dochi=[]
for i in range(R):
    for j in range(C):
        if space[i][j]=='S':
            dochi.append((i,j,0))
            break

answer=False
while True:
    di=[-1,1,0,0]
    dj=[0,0,-1,1]
    water_v=[[False for _ in range(C)]for _ in range(R)]
    dochi_v=[[False for _ in range(C)]for _ in range(R)]
    water=[]
    for i in range(R):
        for j in range(C):
            if space[i][j]=='*' and water_v[i][j]==False:
                water_v[i][j]=True
                for k in range(4):
                    ni=i+di[k]
                    nj=j+dj[k]
                    if 0<=ni<R and 0<=nj<C and space[ni][nj]=='.' and water_v[ni][nj]==False:
                        #이동할 물 넣기
                        water.append((ni,nj))
                        water_v[ni][nj]=True
    # 인접한 물 채우기
    for i,j in water:
        space[i][j]='*'

    find=False
    flag=False
    cannot=False
    #도치의 새로운 이동 범위 넣을 배열
    new_dochi=[]
    if len(dochi)==0:#더이상 움직일 도치가 없는 경우
        cannot=True
        break

    for x,y,time in dochi:
        space[x][y]='.'
        if dochi_v[x][y]==False: # 첫방문 한 애만
            dochi_v[x][y]=True
            for k in range(4):
                nx=x+di[k]
                ny=y+dj[k]
                if (0<=nx<R) and (0<=ny<C):
                    if space[nx][ny]=='D':# 고슴도치 도착
                        find=True
                        time=time+1
                        break
                    if space[nx][ny]=='.' and dochi_v[nx][ny]==False:
                        #도치 이동한 범위 구하기
                        new_dochi.append((nx,ny,time+1))
                        space[nx][ny]='S'

            if find==True: #고슴도치가 하나라도 도착했을 때
                flag=True
                break

    dochi=new_dochi[:]
    if flag==True: #답 찾았을 때
        answer=True
        break


if answer==True:
    print(time)
elif cannot==True:
    print('KAKTUS')



