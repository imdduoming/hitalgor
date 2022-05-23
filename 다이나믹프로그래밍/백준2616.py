# #백준 2616
# #백준 소형기관차 골드4
# import sys
# input=sys.stdin.readline
# N=int(input())
# guests=list(map(int,input().split()))
# k=int(input())
# dp=[0 for i in range(len(guests))]
# if N==0:
#     print(0)
# else:
#     for i in range(k):
#         dp[k-1]+=guests[i]
#     for i in range(k,len(guests)):
#         total=dp[i-k]
#         for j in range(k):
#             total+=guests[i-j]
#         dp[i]=max(dp[i-1],total)
#
#     print(dp[N-1])