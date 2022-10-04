import sys
def operate(num,total,str):
    if str == '+':
        total+=num
    elif str == '-':
        total-=num
    elif str == '*':
        total*=num
    else:
        if total<0:
            total=(-total)//(num)
            return -total
        else:
            total=total//(num)
    return total
def solve(operators,nums):
    total = nums[0]
    for i in range(1,len(nums)):
        total=operate(nums[i],total,operators[i-1])

    return total

from itertools import permutations
input=sys.stdin.readline
N= int(input())
nums = list(map(int,input().split()))
oper_nums = list(map(int,input().split()))
opers=[]
for i in range(0,4):
    if i==0:
        new=['+' for j in range(oper_nums[i])]
    elif i==1:
        new=['-' for j in range(oper_nums[i])]
    elif i==2:
        new=['*' for j in range(oper_nums[i])]
    elif i==3:
        new=['/' for j in range(oper_nums[i])]

    opers+=new
answer=0
max_val=-9999999999
min_val=9999999999
for i in set(permutations(opers,len(opers))):
    answer = solve(i,nums)
    max_val=max(answer,max_val)
    min_val=min(answer,min_val)

print(max_val)
print(min_val)
