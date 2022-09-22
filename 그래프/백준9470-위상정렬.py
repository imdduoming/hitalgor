# 백준 strahler 순서
# 백준 골드 3
from collections import deque
T= int(input())
def bfs(queue,m,p,arr):
    strahler_order = [0] * (m+1)
    max_count_list = [[0, 0] for _ in range(m+1)]
    while queue:
        now =queue.popleft()
        # 현재 노드 Order 계산
        if max_count_list[now][1]==1: # 갯수가 한 개이면
            strahler_order[now]=max_count_list[now][0]
        else:
            strahler_order[now]=max_count_list[now][0]+1
        # max_count 계산
        for i in arr[now]:
            indegree[i]-=1
            if not indegree[i]:
                queue.append(i)
                print(queue)
            if max_count_list[i][0]<strahler_order[now]:
                max_count_list[i][0]=strahler_order[now]
                max_count_list[i][1]=1
            elif max_count_list[i][0] == strahler_order[now]:
                max_count_list[i][1] += 1

    return strahler_order[m]



for i in range(T):
    k,m,p=map(int,input().split())
    arr=[[] for i in range(m+1)]
    indegree = [0] * (m + 1)
    for j in range(p):
        start,end = map(int,input().split())
        arr[start].append(end)
        indegree[end]+=1 # 진입차수 추가
    queue=deque([])

    #진입차수가 0인 것 큐에 넣기
    for i in range(1,m+1):
        if indegree[i]==0:
            queue.append(i)

    # # print(arr)
    # print('start queue',queue)
    print(k,bfs(queue,m,p,arr))


