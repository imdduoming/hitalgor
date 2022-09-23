# 백준 두 용액
# 백준 투포인터 골드 5
import sys

N=int(input())
arr = list(map(int,input().split()))
left=0
right=len(arr)-1
arr.sort()
answer=sys.maxsize
ans=[]
while left!=right:
    left_num , right_num = arr[left],arr[right]
    if abs(left_num+right_num)<answer:
        answer=abs(left_num+right_num)
        ans=[left_num,right_num]
        if answer==0:
            break

    if left_num+right_num<0:
        left+=1
    else:
        right-=1

for i in ans:
    print(i,end=' ')