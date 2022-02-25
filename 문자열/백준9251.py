#백준9251
#골드4 LCS 문자열 알고리즘
import sys
input=sys.stdin.readline
str_a=input().rstrip()
str_b=input().rstrip()
dp=[[0 for i in range(len(str_b)+1)] for j in range(len(str_a)+1)]

for i in range(1,len(str_a)+1):
    for j in range(1,len(str_b)+1):
        # 생성된 두 문자열이 같다면
        if str_a[i-1]==str_b[j-1]:
            # 두문자열이 생성되기전 최대 길이 +1
            dp[i][j]=dp[i-1][j-1]+1
        else:
            # 두문자열이 다르다면 , 각각 문자가 생성되기 전 최대길이 중 최댓값
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])


