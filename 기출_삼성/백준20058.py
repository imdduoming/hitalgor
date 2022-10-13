# 골드 3 삼성 기출
import copy
from collections import deque
def rotate(part,x,y,leng,space):
    new_part = copy.deepcopy(part)
    # print('new_part',new_part)
    #
    for i in range(0,leng):
        for j in range(0,leng):
            space[x+j][y+((leng-1)-i)] = new_part[i][j]
    return space
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def check_ice(space,total_len):
    melting=[]
    for i in range(total_len):
        for j in range(total_len):
            ice_cnt=0
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                if 0<=nx<total_len and 0<=ny<total_len:
                    if space[nx][ny]>0: #얼음이 있는 칸
                        ice_cnt+=1
            if ice_cnt<3 and space[i][j]!=0:
                melting.append((i,j)) # 녹일 얼음 추가

    for x,y in melting:
        space[x][y]-=1

    return space

def biggest_ice(x,y,space):
    global visited
    queue = deque()
    queue.append((x,y))
    cnt=1
    while queue:
        cx,cy = queue.popleft()
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<total_len and 0<=ny<total_len and space[nx][ny]!=0 and not visited[nx][ny]:
                visited[nx][ny]=True
                queue.append((nx,ny))
                cnt+=1

    return cnt

N,Q = map(int,input().split())
total_len = 2**N
space=[]
for i in range(total_len):
    arr = list(map(int,input().split()))
    space.append(arr)
command = list(map(int,input().split()))

for l in command:
    leng = 2 ** l
    for i in range(0,total_len-leng+1,leng):
        for j in range(0,total_len-leng+1,leng):
            part=[]
            for k in range(i,i+leng):
                part.append((space[k][j:j+leng]))

            space= rotate(part,i,j,leng,space)
    space= check_ice(space ,total_len)

visited=[[False for i in range(total_len)] for j in range(total_len)]
max_ans=0
total=0
for i in range(total_len):
    for j in range(total_len):
        if space[i][j]!=0:
            total+=space[i][j]
        if visited[i][j]==False and space[i][j]!=0:
            visited[i][j]=True
            max_ans=max(biggest_ice(i,j,space),max_ans)
print(total)
print(max_ans)