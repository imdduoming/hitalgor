#백준 동전2
#백준 2294 골드 5
n,k = map(int,input().split())
coins=[]
for i in range(n):
    coins.append(int(input()))
dp=[0 for i in range(k+1)]
for i in range(1,k+1):
    arr=[]
    for coin in coins:
        if coin<=i and dp[i-coin]!=-1:
            arr.append(dp[i-coin])
    if not arr:
        dp[i]=-1
    else:
        dp[i]=min(arr)+1
    # print(dp[i])
print(dp[k])