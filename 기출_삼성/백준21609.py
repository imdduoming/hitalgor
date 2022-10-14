import copy
from collections import deque
def find_group(x,y,color):
    global visited
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    queue=deque()
    queue.append((x,y))
    cnt , rcnt =1,0
    block=[(x,y)]
    rainbow=[]
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and space[nx][ny]!=-1 and ((space[nx][ny]==0) or (space[nx][ny]==color)) and not visited[nx][ny]:
                if space[nx][ny]==0: #무지개 블록
                    rcnt+=1
                    rainbow.append((nx,ny))
                cnt+=1
                block.append((nx,ny))
                queue.append((nx,ny))
                visited[nx][ny]=True
    # print('block',block)
    block.sort(key=lambda x:(x[0],x[1]))
    for a,b in rainbow:
        visited[a][b]=False
    if cnt==1:
        return block ,1,0,False
    else:
        return block,cnt,rcnt,True

def eliminate(block):
    global total_score
    global space
    total_cnt = len(block)
    total_score += ((total_cnt)**2 )#점수 획득
    for i,j in block:
        space[i][j]=-2 #빈칸

def gravity():
    global space
    for i in range(N):
        for j in range(N-2,-1,-1):
            block= space[j][i]
            if block >= 0: #일반이거나 무지개
                x=j
                while True:
                    x+=1
                    if x>=N: #격자 범위 벗어나면
                        break
                    if space[x][i]!=-2: #빈칸 아니면
                        break

                if x-1>j:
                    space[j][i]=-2
                    space[x-1][i]=block


def rotate(space): #반시계 방향 90도 회전
    new_space = copy.deepcopy(space)
    for i in range(N):
        for j in range(N):
            new_space[i][j]=space[j][(N-1)-i]
    return new_space


N,M = map(int,input().split())
space=[]
for i in range(N):
    arr = list(map(int,input().split()))
    space.append(arr)

max_block =[]
total_score = 0
while True:
    visited =[[False for a in range(N)]for b in range(N)]
    group_flag =False
    max_cnt , max_rcnt  = 0,0
    for i in range(N):
        for j in range(N):
            if space[i][j]>0 and not visited[i][j]:
                visited[i][j]=True
                block,cnt,rcnt,flag= find_group(i,j,space[i][j])
                if flag==True:
                    group_flag=True
                    if max_cnt<cnt: # 우선순위
                        max_cnt=cnt
                        max_rcnt=rcnt
                        max_block=block

                    elif max_cnt == cnt:
                        if max_rcnt <= rcnt:
                            max_cnt=cnt
                            max_rcnt=rcnt
                            max_block=block


    if group_flag==False : #그룹 더이상 만들 수 없다면 종료
        break

    eliminate(max_block)
    gravity()
    new_space = rotate(space)
    space = copy.deepcopy(new_space)
    gravity()

print(total_score)