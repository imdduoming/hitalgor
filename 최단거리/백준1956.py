import sys

input=sys.stdin.readline
V,E=map(int,input().split())
INF = sys.maxsize
load=[[INF for i in range(V+1)] for j in range(V+1)]
for i in range(E):
    start,end,dist=map(int,input().split())
    load[start][end]=dist

for i in range(1,V+1):
    for j in range(1,V+1):
        for k in range(1,V+1):
            load[j][k]=min(load[j][i]+load[i][k],load[j][k])


answer=INF
for i in range(1,V+1):
        answer=min(load[i][i],answer)

if answer==INF:
    print(-1)
else:
    print(answer)
