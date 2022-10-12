def dfs(team,score,total,C,idx):
    if score>C:
        return
    if score<=C and len(team)==idx:
        answer.append(total)
        return
    # 추가
    dfs(team,score+team[idx][0],total+team[idx][0]**2,C,idx+1)
    # 추가 안함
    dfs(team,score,total,C,idx+1)

def solve(team1,team2,C): #이득계산

    global answer
    global max_honey
    answer=[]
    dfs(team1,0,0,C,0)

    max1=max(answer)
    answer=[]
    dfs(team2,0,0,C,0)

    max2=max(answer)
    if max1 + max2 > max_honey:
        max_honey = max1+max2
    return


def find_team2(team1,N,M,C):
    global max_ans
    for i in range(0,N):
        for j in range(0,N-M+1):
            team2=[]
            flag=False
            for k in range(j,j+M):
                if (arr[i][k],i,k) in team1: # team1 중복
                    flag=True
                    break
                else:
                    team2.append((arr[i][k],i,k))
            if flag==False:
                solve(team1,team2,C)
T=int(input())
for test_case in range(1,T+1):
    N,M,C = map(int,input().split())
    arr=[]
    for i in range(N):
        a = list(map(int,input().split()))
        arr.append(a)
    max_honey=0
    for i in range(0,N):
        for j in range(0,N-M+1):
            team1=[]
            for k in range(j,j+M):
                team1.append((arr[i][k],i,k))
            find_team2(team1,N,M,C)
    print('#',end='')
    print(test_case,max_honey)