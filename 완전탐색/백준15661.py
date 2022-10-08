import sys

def dfs(idx,n):
    global min_diff
    if idx == n:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        # print(visited)
        min_diff = min(min_diff, abs(power1-power2))
        # print('n',n,abs(power1-power2),min_diff)
        return

    visited[idx] = True
    dfs(idx+1,n)
    visited[idx] = False
    dfs(idx+1,n)

input=sys.stdin.readline
N = int(input())
visited = [False for _ in range(N)]
graph = [list(map(int, input().split())) for _ in range(N)]
min_diff = int(1e9)

dfs(0,N)
print(min_diff)