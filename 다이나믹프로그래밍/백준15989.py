
#백준 실버1 1,2,3 더하기 4
T=int(input())
dp=[1 for i in range(10001)]
dp[0]=1
dp[1]=1

for i in range(2,10001):
    dp[i]+=dp[i-2]

for i in range(3,10001):
    dp[i]+=dp[i-3]

for i in range(T):
    n=int(input())
    print(dp[n])