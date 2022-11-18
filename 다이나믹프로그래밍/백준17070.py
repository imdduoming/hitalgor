#파이프옮기기1
#골드5
N=int(input())
space=[]
for i in range(N):
    arr=list(map(int,input().split()))
    space.append(arr)
dp=[[[0 for _ in range(N)] for _ in range(N)]for _ in range(N)]
dp[0][0][1]=1
#가로 줄은 방법의 수 다 1
for i in range(2,N):
    if space[0][i]==0:
        dp[0][0][i]=dp[0][0][i-1]

# 놓여있는 방향에 따라 방법의 수 정하기
for i in range(1,N):
    for j in range(1,N):
        #대각선방향으로 놓여있음
        if space[i-1][j]==0 and space[i][j]==0 and space[i][j-1]==0:
            dp[2][i][j]=dp[0][i-1][j-1]+dp[1][i-1][j-1]+dp[2][i-1][j-1]
        if space[i][j]==0:
            #가로로 놓여있는 경우 어떻게 올 수 있는가 가로-> 가로 / 대각선 ->가로
            dp[0][i][j]=dp[0][i][j-1]+dp[2][i][j-1]
            #세로로 놓여있는 경우 어떻게 올 수 있는가 세로-> 세로 / 대각선 ->세로
            dp[1][i][j]=dp[1][i-1][j]+dp[2][i-1][j]
        # print(dp)
print(dp[0][N-1][N-1]+dp[1][N-1][N-1]+dp[2][N-1][N-1])
