N=int(input())
scv=list(map(int,input().split()))
if len(scv)==1:
    scv=scv+[0,0]
elif len(scv)==2:
    scv.append(0)
print(scv)
dp = [[[0]*61 for _ in range(61)] for _ in range(61)] #각 위치에 도달하는 횟수 저장
obj=[(9,3,1),(9,1,3),(3,1,9),(3,9,1),(1,3,9),(1,9,3)]
dp[scv[0]][scv[1]][scv[2]]=1 #원래 0인데 1로 초기화해서
for i in range(60,-1,-1):
    for j in range(60,-1,-1):
        for k in range(60,-1,-1):
            if dp[i][j][k]>0:
                for o in obj:
                    if i-o[0]>=0:
                        ni=i-o[0]
                    else:
                        ni=0
                    if j-o[1]>=0:
                        nj=j-o[1]
                    else:
                        nj=0
                    if k-o[2]>=0:
                        nk=k-o[2]
                    else:
                        nk=0
                    if dp[ni][nj][nk]==0 or dp[ni][nj][nk]>(dp[i][j][k]+1):
                        dp[ni][nj][nk]=dp[i][j][k]+1
print(dp[0][0][0]-1)


