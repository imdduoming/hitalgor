def solution(dist):
    answer = []
    max_val=0
    end_arr=[]
    for i in range(0,len(dist)):
        max_val = max(max_val,max(dist[i]))

    for i in range(0,len(dist)):
        for j in range(0,len(dist[i])):
            if max_val==dist[i][j]:
                end_arr.append((i,j))


    for start,end in end_arr:
        visited=[-1 for i in range(len(dist))]
        arr=[start]
        visited[start]=1
        visited[end]=1
        next_start=dist[start][end]
        while len(arr)<(len(dist)-1):
            next_start = next_start = dist[start][end]
            for i in range(0,len(dist[start])):

                if visited[i]==-1:
                    if dist[start][i]<=next_start:
                        next_start=dist[start][i]
                        next_idx=i

            arr.append(next_idx)
            visited[next_idx]=1

        arr.append(end)
        answer.append(arr)
    return answer


print(solution([[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]))