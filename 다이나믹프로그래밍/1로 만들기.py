#1로 만들기
N=int(input())
dp=[0]*1000001
num=N
for i in range(2,N+1):
    a,b,c=1000000,1000000,1000000
    if i%3==0:
        a =dp[i//3]+1
    if i%2==0:
        b = dp[i // 2] + 1
    c = dp[i -1] + 1
    dp[i]=min(a,b,c)

print(dp[N])
