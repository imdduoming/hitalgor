# 백준 치킨배달 골드 5
import sys
from itertools import combinations

def dfs():
    global answer
    for i in combinations(chicken,M):
        total_dist=0
        for j in house:
            hx,hy =j[0],j[1]
            house_dist=sys.maxsize
            #집마다 최소의 치킨거리 구해서 도시거리 구하기
            for k in i:
                cx,cy=k[0],k[1]
                dist=abs(hx-cx)+abs(hy-cy)
                house_dist=min(house_dist,dist)
            total_dist+=house_dist
        answer=min(answer,total_dist)



N,M= map(int,input().split())
city=[]
for i in range(N):
    arr=list(map(int,input().split()))
    city.append(arr)
house=[]
chicken=[]
for i in range(N):
    for j in range(N):
        if city[i][j]==1:
            house.append((i,j))
        elif city[i][j]==2:
            chicken.append((i,j))

visited= [False for i in range(len(chicken))]
answer=sys.maxsize
dfs()
print(answer)


