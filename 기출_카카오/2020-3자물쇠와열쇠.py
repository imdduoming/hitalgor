def rotate(key,d):
    new_key = [[0 for i in range(len(key))]for j in range(len(key))]
    N = len(new_key)-1

    if d%4 ==1:
        # 90도 회전
        for i  in range(len(new_key)):
            for j in range(len(new_key)):
                new_key[i][j] = key[j][N-i]
    elif d%4 ==2:
        # 180도 회전
        for i  in range(len(new_key)):
            for j in range(len(new_key)):
                new_key[i][j] = key[N-i][N-j]
    elif d%4 ==3:
        # 270도 회전
        for i  in range(len(new_key)):
            for j in range(len(new_key)):
                new_key[i][j] = key[N-j][i]
    else:
        for i  in range(len(new_key)):
            for j in range(len(new_key)):
                new_key[i][j] = key[i][j]
    return new_key

def correct(new_key , large_lock,i,j,M,N):
    # 열쇠와 자물쇠가 맞는지 판단하는 함수
    print(new_key)
    is_lock=False
    answer=True
    new_lock = [[0 for _ in range(N*3)]for _ in range(N*3)]
    # 새로운 자물쇠 생성
    for a in range(N, N+N):
        for b in range(N, N+N):
            # print(i,j)
            new_lock[a][b] = large_lock[a][b]
    for x in range(i,i+M):
        for y in range(j,j+M):
            print('x',x,'y',y)
            if N<=x<2*N and N<=y<2*N:
                print("범위들어옴",x,y)
                print('new_key',new_key[x-i][y-j])
                print('large_lock',new_lock[x][y])
                if (new_key[x-i][y-j] == new_lock[x][y]) and (new_key[x-i][y-j]==0):
                    answer=True
                elif (new_key[x-i][y-j] == new_lock[x][y]) and (new_key[x-i][y-j]==1) :
                    is_lock =True
                    new_lock[x][y]=2
                    answer=True
                else:
                    return False

    print('a',answer)
    print('is',is_lock)
    print(new_lock)
    if answer ==True:
        if is_lock:
            answer =True
        else:
            return False

    if is_lock == True:
        for a in range(N, N+N):
            for b in range(N, N+N):
                # print(i,j)
                if new_lock[a][b]==1:
                    return False

    return answer


def solution(key, lock):
    answer = True
    total=0
    M,N = len(key),len(lock)
    # 큰 자물쇠 만들기
    for i in range(len(lock)):
        total+=sum(lock[i])
    if total == (N*N):
        return True

    large_lock = [[0 for i in range(N*3)]for j in range(N*3)]

    for i in range(0,N):
        for j in range(0,N):
            if lock[i][j] == 0:
                large_lock[i+N][j+N]=1
            else:
                large_lock[i+N][j+N]=0

    for i in range(N-M+1,N+N):
        for j in range(N-M+1,N+N):
            for d in range(0,4):
                # 키를 한 방향씩 회전
                print('i',i,'j',j)
                new_key = rotate(key,d)
                if correct(new_key,large_lock,i,j,M,N):
                    return True

    return False

print(solution([[1,1,1], [1, 1,1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]))