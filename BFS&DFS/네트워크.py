visited = list()


def solution(n, computers):
    global visited
    visited = [False] * n

    answer = 0

    for i in range(n):
        if not visited[i]:
            dfs(n, computers, i)
            answer += 1

    return answer


def dfs(n, computers, start):
    global visited, count

    visited[start] = True
    for i in range(n):
        if computers[start][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(n, computers, i)