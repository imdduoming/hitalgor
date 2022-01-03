def solution(rows, columns, queries):
    result = []
    graph = [[0] * columns for i in range(rows)]
    for i in range(len(graph)):
        for j in range(0,len(graph[i])):
            graph[i][j]=(i)*columns+(j+1)
    for i in queries:
        x1 = i[0]-1
        y1 = i[1]-1
        x2 = i[2]-1
        y2 = i[3]-1
        #맨위
        tmp=graph[x1][y1]
        small=tmp
        for i in range(x1+1,x2+1):
            graph[i-1][y1]=graph[i][y1]
            small=min(small,graph[i][y1])
        for j in range(y1+1,y2+1):
            graph[x2][j-1] = graph[x2][j]
            small = min(small, graph[x2][j])
        for i in range(x2-1,x1-1,-1):
            graph[i+1][y2]=graph[i][y2]
            small = min(small, graph[i][y2])
        for j in range(y2-1,y1-1,-1):
            graph[x2][j+1]=graph[x2][j]
            small = min(small, graph[x2][j])
        #첫번째 옆칸을 첫번재 값으로 대입
        graph[x1][y1+1]=tmp

        result.append(small)


    return result