import sys

input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0


def dfs(now, cnt, num, total):
    global answer
    visited[now] = 1

    if cnt == num:
        if total == S:
            print(now,arr[now])
            answer += 1
        total = 0

    for i in range(N):
        if not visited[i]:
            print(i)
            dfs(i, cnt + 1, num, total + arr[now])

for i in range(N):
    visited=[0]*N
    dfs(0,1,arr[i])
print(answer)