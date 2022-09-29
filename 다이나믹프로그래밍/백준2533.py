# 백준 사회망서비스
# 백준 골드3
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N=int(input())
tree= [[] for a in range(N+1)]
for i in range(N-1):
    start, end = map(int,input().split())
    tree[start].append(end)


def dfs(node):
    # 트리의 단말 노드부터 진행
    visited[node]=True
    dp[node][0],dp[node][1]=0,1
    for child in tree[node]:
        if not visited[child]:
            dfs(child)
            dp[node][0]+=dp[child][1] #내가 얼리어답터가 아닐 때 자식은 얼리어답터여야함
            dp[node][1]+=min(dp[child][0],dp[child][1]) #내가 얼리어답터일때 자식이 얼리어답터이든 아니든 상관 없음
dp=[[0,0] for i in range(N+1)]
visited=[False for i in range(N+1)]
dfs(1)
print(min(dp[1]))