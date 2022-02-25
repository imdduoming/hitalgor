#평범한 배낭
#백준 12865
N,K=map(int,input().split())
array=[(0,0)]
for i in range(N):
    weight,value=map(int,input().split())
    array.append((weight,value))
dp=[0]*(K+1)
for i in range(1,N+1):
    weight=array[i][0]
    val=array[i][1]
    for j in range(1,K+1):
            #새로운 물건을 넣는 것과 안넣는 경우의 가치 중 최댓 값
            if j>=weight:
                dp[j]=max(dp[j],dp[j-weight]+val)
                print(j,dp[j])

print(dp[K])