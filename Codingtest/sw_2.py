#시험자료
N=int(input())
cal=list(map(int,input().split()))
visited=[0]*2500

result=0
def dfs(start,cnt,visited,total,answer):

    if cnt==3:

        if 2000<=total<=2500:
            answer+=1

        return
    for i in range(start+1,N):
        total+=cal[i]
        dfs(i,cnt+1,visited,total)
        total-=cal[i]

    return answer
for i in range(0,N):
    answer=0
    answer=dfs(i,1,visited,cal[i])
    result+=answer
print(result)