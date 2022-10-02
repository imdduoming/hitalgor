
def bfs(x,y,maps ,visited,N,M):
    from collections import deque
    queue = deque([])
    queue.append((x,y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    country={}
    country[maps[x][y]]=1
    visited[x][y]=True
    while queue:
        cx,cy=queue.popleft()
        for i in range(4):
            nx=dx[i]+cx
            ny=dy[i]+cy
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False and maps[nx][ny]!='.':
                if maps[nx][ny] not in country:
                    country[maps[nx][ny]]=1
                else:
                    country[maps[nx][ny]]+=1
                queue.append((nx,ny))
                visited[nx][ny]=True

    new_country=sorted(country.items(),key = lambda item: item[1],reverse=True)
    victory_c = new_country[0][0]
    victory_cnt = new_country[0][1]
    for k,v in new_country:
        if v>=victory_cnt:
            if k>victory_c:
                victory_c=k
                victory_cnt=v


    sum=0
    print('victory')
    for i in range(0,len(new_country)):
        new_country[i]=list(new_country[i])
        if victory_c!=new_country[i][0]:
            now_c=new_country[i][0]
            now_cnt=new_country[i][1]
            if now_cnt<victory_cnt:
                sum+=now_cnt
                new_country[i][1]=0
        else:
            victory_idx=i
    new_country[victory_idx][1]+=sum
    print('최종',new_country)
    return new_country,visited

def total_ground(ground,new_country):
    for i in range(len(new_country)):
        c= new_country[i][0]
        cnt=new_country[i][1]
        if c not in ground:
            ground[c]=cnt
        else:
            ground[c]+=cnt
    return ground

def solution(maps):
    answer = 0
    N = len(maps)
    M=len(maps[0])
    visited=[[False for i in range(M)] for j in range(N)]
    ground={}
    for i in range(0,N):
        for j in range(0,M):
            if maps[i][j]!='.' and visited[i][j]==False:
                new_c, visited = bfs(i,j,maps,visited,N,M)
                ground=total_ground(ground,new_c)

    return max(list(ground.values()))

print(solution(["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"]))