from collections import deque
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
visited=[-1 for i in range(N+1)]
total_nums=[]

def select(start,cnt,nums):

    if cnt==M:
        total_nums.append(nums[:])
        return

    for i in range(1,N+1):
        if visited[i]==-1:
            nums.append(i)
            visited[i]=1
            select(i,cnt+1,nums)
            visited[i]=-1
            nums.pop()

    return total_nums
total_nums=select(0,0,[])
for select in total_nums:
    for i in select:
        print(i,end=' ')
    print()
