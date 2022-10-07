# 백준 톱니바퀴
# 골드 5
def rotate(target,dir,wheel):
    if dir ==1: # 시계방향
        # print('시계')
        tmp= wheel[target][7]
        for t in range(8):
            new = wheel[target][t]
            wheel[target][t]=int(tmp)
            tmp = new

    else:
        # 반시계방향
        # print('반시계')
        start= wheel[target][0]
        for t in range(1,8):
            new = int(wheel[target][t])
            wheel[target][t-1]=new

        wheel[target][-1]=int(start)
    return wheel

def get_score(wheel):
    total=0

    if wheel[0][0]==1:
        total+=1
    if wheel[1][0]==1:
        total+=2
    if wheel[2][0]==1:
        total+=4
    if wheel[3][0]==1:
        total+=8

    return total

def solve(target,dir,wheel):
    left_t=target
    right_t = target
    left_dir =dir
    right_dir =dir
    left_w=wheel[left_t][6]
    right_w=wheel[right_t][2]
    while left_t>=1:
        # print('left_t',left_t)
        if left_w!=wheel[left_t-1][2]:
            #방향 다르면 반대방향으로 회전
            left_w=wheel[left_t-1][6]
            wheel= rotate(left_t-1,-left_dir,wheel)
            left_dir=-left_dir
            # print('왼쪽회전결과',left_t-1,wheel[left_t-1])
            left_t-=1
        else:
            # print('회전안함')
            break

    while right_t<=2:
        # print('right_t',right_t)
        if right_w!=wheel[right_t+1][6]:
            right_w=wheel[right_t+1][2]
            wheel= rotate(right_t+1,-right_dir,wheel)
            right_dir = -right_dir
            # print('오른쪽회전결과',right_t+1,wheel[right_t+1])
            right_t+=1
        else:
            # print('회전안함')
            break

    wheel = rotate(target,dir,wheel)
    # print('wheel',wheel)
    return wheel

wheel =[]
for i in range(4):
    str =list(map(int,input()))
    wheel.append(str)


total=0
T=int(input())
for i in range(T):
    num,dir = map(int,input().split())
    wheel = solve(num-1,dir,wheel)

total+= get_score(wheel)
print(total)