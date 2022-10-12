def make_route(sx,sy,x,y,dir,cnt,road,visited):
    dx =[1,1,-1,-1]
    dy =[1,-1,-1,1]
    global ans
    if ((sx==x) and (sy==y)) and cnt!=0:
        # 시작점과 같지만 1개 카페만 돈 경우는 아님
        total=sum(visited)
        # print(visited)
        # print('total',total)
        ans=max(ans,total)
        return
    if x<0 or x>=N or y<0 or y>=N:
        return
    if visited[road[x][y]]:
        return
    else:
        visited[road[x][y]]=1
        # print('visited',visited)
        make_route(sx,sy,x+dx[dir],y+dy[dir],dir,cnt+1,road,visited) #방향 그대로
        if dir+1<4:
            make_route(sx,sy,x+dx[dir+1],y+dy[dir+1],dir+1,cnt+1,road,visited) #방향 꺾기
        visited[road[x][y]]=0



T=int(input())
for t in range(1,T+1):
    N=int(input())
    road=[]
    for i in range(N):
        arr = list(map(int,input().split()))
        road.append(arr)
    ans=0
    for i in range(0,N-1):
        for j in range(1,N-1):
            visited=[0 for i in range(0,101)]
            make_route(i,j,i,j,0,0,road,visited)
    if ans==0:
        print('#{} {}'.format(t, -1))
    else:
        print('#{} {}'.format(t, ans))
