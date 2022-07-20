# 백준 2531
# 백준 실버1
import sys
from collections import deque
input=sys.stdin.readline
N,d,k,c=map(int,input().split())
dish=[]
for i in range(N):
    num=int(input())
    dish.append(num)

left=0
right=0
res=0
while left!=N:
    right=left+k
    num=set()
    add=1
    for i in range(left,right):
        i%=N
        num.add(dish[i])
        if dish[i]==c:
            add=0
    ans=len(num)
    if add==1:
        ans+=1
    res=max(ans,res)
    left+=1

print(res)

