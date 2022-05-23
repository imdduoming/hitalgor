#백준16197 골드 4
#백준 두 동전
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
board=[]
for i in range(N):
    arr=list(input().rstrip())
    board.append(arr)
#구슬 위치 찾기
loc=[]
for i in range(N):
    for j in range(M):
        if board[i][j]=='o':
            loc.append((i,j))
            if len(loc)==2:
                break
a_x,a_y=loc.pop()
b_x,b_y=loc.pop()
ans=sys.maxsize
visited_a=[[False for i in range(M)]for j in range(N)]
visited_b=[[False for i in range(M)]for j in range(N)]
def move(a_x,a_y,b_x,b_y,cnt):
    global ans
    if cnt>10:
        #10이 넘어가는 경우임 ,
        return
    if cnt>=ans:
        return
    if a_x==b_x and a_y==b_y:
        #구슬의 위치가 같아짐 이방법으로는 하나만 떨어뜨릴 수 없음
        return
    # print('현재 구슬 위치','구슬 a',a_x,a_y,'구슬 b',b_x,b_y)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited_a[a_x][a_y]=True
    visited_b[b_x][b_y]=True
    for i in range(4):
        a_nx=a_x+dx[i]
        a_ny=a_y+dy[i]
        b_nx = b_x + dx[i]
        b_ny = b_y + dy[i]
        # print('이동 구슬 위치', '구슬 a', a_nx, a_ny, '구슬 b', b_nx, b_ny)
        if ((a_nx<0 or a_nx>=N) or (a_ny<0 or a_ny>=M)) and ((b_nx<0 or b_nx>=N) or (b_ny<0 or b_ny>=M)):
            #구슬 둘다 떨어지는 경우
            # print('구슬 둘다 떨어짐')
            continue
        elif  ((a_nx<0 or a_nx>=N) or (a_ny<0 or a_ny>=M)) or ((b_nx<0 or b_nx>=N) or (b_ny<0 or b_ny>=M)):
            # print('현재 ans',ans)
            # print('현재 cnt', cnt)
            # print('구슬백준 하나만 떨어짐')
            ans=min(ans,cnt)
            # print('현재 ans',ans)
        else:
            # print('구슬 안떨어짐')
            #구슬이 떨어지지 않은 경우
            if board[a_nx][a_ny] == '#' and board[b_nx][b_ny] == '#':
                continue

            else:
                if board[a_nx][a_ny] == '#':
                    a_nx = a_x
                    a_ny = a_y
                if board[b_nx][b_ny] == '#':
                    b_nx = b_x
                    b_ny = b_y
                # print('다음 구슬 위치', '구슬 a', a_nx, a_ny, '구슬 b', b_nx, b_ny)
                if visited_a[a_nx][a_ny]==False or visited_b[b_nx][b_ny]==False:
                    move(a_nx, a_ny, b_nx, b_ny, cnt+1)
                    visited_a[a_nx][a_ny]=False
                    visited_b[b_nx][b_ny]=False

    return ans
res=move(a_x,a_y,b_x,b_y,1)
if res==sys.maxsize:
    print(-1)
else:
    print(res)