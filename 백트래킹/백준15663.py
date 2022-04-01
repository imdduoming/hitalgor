from collections import deque
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
input_nums=list(map(int,input().split()))
#중복제거

input_nums.sort()
max_num=max(input_nums)
visited=[-1]*N

total_nums=[]

def select(start,cnt,nums):

    if cnt==M:
        total_nums.append(tuple(nums[:]))
        return

    for i in range(0,len(input_nums)):
        if visited[i]==-1:
            nums.append(input_nums[i])
            visited[i]=1
            select(input_nums[i],cnt+1,nums)
            visited[i]=-1
            nums.pop()

    return total_nums
total_nums=select(0,0,[])

answer=[]
total_nums=sorted(list(set(total_nums)))
for select in total_nums:
    for i in select:
        print(i,end=' ')
    print()