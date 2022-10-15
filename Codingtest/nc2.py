import sys
graph =[[],[2,3],[1,3],[1,2,4,5],[3,5],[3,4,6,7],[5,7],[5,6,8],[7,9,10],[8,10],[8,9,11,12],[10,12],[10,11]]
print(len(graph))
dist = sys.maxsize
def go(now,end,cnt,visited):
    print('now',now,'end',end,'cnt',cnt)
    print('graph 현재 방문 가능',graph[now])
    global dist
    global ans
    if now==end:
        dist=min(dist,cnt)

        print('종료')
        print('now',now,'end',end,'cnt',cnt)
        print('dist',dist)

        return
    for i in graph[now]:
        if visited[i]==False:
            visited[i]=True
            go(i,end,cnt+1,visited)
            visited[i]=False


def solution(music):
    now=1
    answer=0
    global dist
    global ans
    for i in range(len(music)):
        visited =[False for i in range(13)]
        dist =sys.maxsize

        go(now,music[i],0,visited)

        answer+=dist
        now=music[i]

    return answer

print(solution([10,4,5,9,12]))