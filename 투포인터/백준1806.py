# 백준 부분합
# 투포인터 골드4
import sys
N,S= map(int,input().split())
arr = list(map(int,input().split()))
left=0
right =0
now = 0
ans = sys.maxsize

while True:
    if now>=S:
        ans=min(ans,(right-left))
        now-=arr[left]
        left+=1
    elif right==N:
        break
    else:
        now+=arr[right]
        right+=1

if ans == sys.maxsize:
    print(0)
else:
    print(ans)