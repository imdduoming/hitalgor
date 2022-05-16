def solution(n, s, a, b, fares):
    import sys
    answer=sys.maxsize
    route=[[answer for i in range(n+1)]for j in range(n+1)]
    for i in range(1,n+1):
        route[i][i]=0
    for i,j,k in fares:
        route[i][j]=k
        route[j][i]=k

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if route[i][k]!=-1 and route[k][j]!=-1:
                    route[i][j]=min(route[i][j],route[i][k]+route[k][j])

    for k in range(1,n+1):
        answer=min(answer,route[s][k]+route[k][a]+route[k][b])
    return answer