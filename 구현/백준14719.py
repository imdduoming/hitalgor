# 백준 빗물 골드5
H,W = map(int,input().split())
space = list(map(int,input().split()))
ans=0
for i in range(1,W-1):
    left = max(space[:i])
    right = max(space[i+1:])

    min_heignt = min(left,right)
    if space[i]<min_heignt:
        ans+=min_heignt-space[i]

print(ans)