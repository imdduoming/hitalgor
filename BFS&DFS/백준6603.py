#로또
#BFS&DFS/DFS
def dfs(level, s, visited,answer):
    if len(answer) == 6:
        for i in answer:
            print(i,end=' ')
        print()
        return


    else:
        #백트래킹
        for i in range(level,len(s)):
            if not visited[s[i]]:

                visited[s[i]] = 1
                answer.append(s[i])
                dfs(i+1, s, visited,answer) #가장 마지막 단계에서 index 길이 =6 이 되어서 종료됨
                answer.pop()

                visited[s[i]] = 0 # 마지막 단계의 숫자는 방문처리 0으로 해줌



while True:
    s = list(map(int, input().split()))
    if s[0] == 0: #입력이 0이면 종료
        break

    visited=[0]*50
    del s[0]
    answer=[]

    dfs(0,s,visited,answer)
    print()

