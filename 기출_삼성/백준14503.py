#로봇청소기
n,m = map(int,input().split())
r,c,nd=map(int,input().split())
space=[]
for i in range(n):
    arr=list(map(int,input().split()))
    space.append(arr)

dx=[-1,0,1,0]
dy=[0,-1,0,1]
d =[[0] * m for _ in range(n)]
d[r][c]=1

cnt=1
a2=0#4번되면 조건실행


while True:
    nd=(nd+1)%4
    nr=r+dx[nd]
    nc=c+dy[nd]
    if d[nr][nc]==0 and space[nr][nc]==0:
        d[nr][nc]=1
        r=nr
        c=nc
        a2=0
        cnt+=1 #청소횟수 증가
        continue

    #그렇지 않을 경우, 왼쪽 방향으로 회전한다. 이때, 왼쪽은 현재 바라보는 방향을 기준으로 한다.
    else: #이동불가능
        a2+=1
    #1번으로 돌아가거나 후진하지 않고 2a번 단계가 연속으로 네 번 실행되었을 경우, 바로 뒤쪽이 벽이라면 작동을 멈춘다. 그렇지 않다면 한 칸 후진한다.
    if a2==4:
        nr=r-dx[nd]
        nc=c-dy[nd]

        if space[nr][nc]==0:
            r=nr
            c=nc
        else:
            break
        a2=0

print(cnt)







