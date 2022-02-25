import sys
import heapq
input=sys.stdin.readline
N=int(input())
array=[]
for i in range(N):
    row=list(map(int,input().split()))
    array.append(row)

for i in range(N):
    for j in range(N):
        if array[i][j]==9:
            x,y,size,cnt,time=i,j,2,0,0
            break


def find(x, y, size, cnt,time):
    visited = [[-1 for i in range(N)] for j in range(N)]
    visited[x][y] = 1
    array[x][y]=0
    time=0
    heap=[]

    heapq.heappush(heap,(time,x,y,size))
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    while heap:
        time,x,y,size = heapq.heappop(heap)
        if array[x][y] !=0 and array[x][y]< size:
            array[x][y] = 0
            cnt += 1

            return x, y, size, cnt, time
        for j in range(4):
            next_x = x + dx[j]
            next_y = y + dy[j]

            if 0 <= next_x < N and 0 <= next_y < N and visited[next_x][next_y] == -1 and array[next_x][next_y] <= size:
                if array[next_x][next_y] == 0 or array[next_x][next_y] <= size:
                    heapq.heappush(heap,(time+1,next_x,next_y,size))
                    visited[next_x][next_y]=1


    return -1, -1, size,cnt,0

flag=0
total=0
while x<N and y<N:

    x,y,size,cnt,time=find(x,y,size,cnt,total)
    total+=time
    if cnt == size:
        size += 1
        cnt = 0

    if x==-1 and y==-1:
        print(total)
        flag=1
        break
if flag==0:
    print(total)
