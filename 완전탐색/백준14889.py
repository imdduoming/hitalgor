import sys
from itertools import combinations

def divide_team(teams):
    t1 ={}
    t2={}
    for i in range(1,N+1):
        if i in teams:
            t1[i]=1
        else:
            t2[i]=1
    return t1,t2

def get_score(arr,t1,t2):
    t1_score , t2_score = 0,0
    for i,j in combinations(t1,2):
        t1_score +=arr[i-1][j-1]
        t1_score +=arr[j-1][i-1]
    for i,j in combinations(t2,2):
        t2_score +=arr[i-1][j-1]
        t2_score +=arr[j-1][i-1]
    return abs(t2_score-t1_score)


score=[]
N=int(input())
for i in range(N):
    arr = list(map(int,input().split()))
    score.append(arr)
teams = [i for i in range(1,N+1)]
team = list(combinations(teams,N//2))

ans=sys.maxsize
for i in range(0,len(team)//2):
    team1,team2 = divide_team(team[i])
    ans = min(ans, get_score(score,team1,team2))

print(ans)