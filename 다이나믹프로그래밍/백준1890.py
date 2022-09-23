N=int(input())
jump = []
for i in range(N):
    arr=list(map(int,input().split()))
    jump.append(arr)
dp =[[0 for i in range(N)]for j in range(N)]
visited=[[False for i in range(N)]for j in range(N)]
visited[0][0]=True
dp[0][0]=1
for i in range(N):
    for j in range(N):
        if i==(N-1) and j==(N-1):
            break
        if visited[i][j]==True:
            # print('i',i)
            # print('j',j)
            if (j+jump[i][j])<N:
                dp[i][j+jump[i][j]]+=(dp[i][j])
                visited[i][j+jump[i][j]]=True
                # print(dp[i][j+jump[i][j]])
            if (i+jump[i][j])<N:
                dp[i+jump[i][j]][j]+=(dp[i][j])
                visited[i+jump[i][j]][j]=True
            #     print(dp[i+jump[i][j]][j])
            # print(dp)
print(dp[N-1][N-1])