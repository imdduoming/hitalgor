from typing import List
def fire(i,j,m,n,answer):
    for a in range(i-m,i+m+1):
        for b in range(j-m,j+m+1):
            if 0<=a<n and  0<=b<n:
                answer[a][b]+=1
def ice(i,j,m,n,answer):
    start,end=i,i
    for a in range(i-m,i+m+1):
        for c in range(start,end+1):
            if 0<=a<n and  0<=c<n:
                answer[a][c]-=1
        if 0== start and end== n-1:
            start+=1
            end-=1
        else:
            start-=1
            end+=1



def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
    answer = [[0 for i in range(n)] for j in range(n)]
    totem = [[0 for i in range(n)] for j in range(n)]
    for i,j in fires:
        answer[i-1][j-1]=1
        totem[i-1][j-1]=1
    for i,j in ices:
        answer[i-1][j-1]=-1
        totem[i-1][j-1]=-1
    for i in range(n):
        for j in range(n):
            if totem[i][j]==1:
                fire(i,j,m,n,answer)
            elif totem[i][j]==-1:
                ice(i,j,m,n,answer)

    return answer

print(solution(3,2,[[1,1]],[[3,3]]))