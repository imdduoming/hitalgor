import sys

input = sys.stdin.readline
from collections import deque

graph = []
N, M, K = map(int, input().split())
# 땅 초기 양분
ground = [[0 for i in range(N + 1)]]
for i in range(N):
    arr = [0]
    arr = arr + [5 for i in range(N)]
    ground.append(arr)

# 겨울에 추가할 양분
add = [[0 for i in range(N + 1)]]
for i in range(N):
    arr = [0]
    arr += list(map(int, input().split()))
    add.append(arr)

tree = [[deque() for i in range(N + 1)] for j in range(N + 1)]
for i in range(M):
    x, y, age = map(int, input().split())
    tree[x][y].append(age)


def spring(tree, ground):
    dead_tree = []
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # 나이가 어린 나무부터 양분을 먹는다. 내림차순으로 정렬해서 뒤에서부터 순회

            for k in range(0,len(tree[i][j])):

                # 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
                eat = tree[i][j][k]
                # 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
                if ground[i][j] - eat < 0:
                    # 나무죽음
                    for m in range(k,len(tree[i][j])):
                        dead_tree.append((i, j, tree[i][j].pop() // 2))
                    break
                else:

                    ground[i][j] -= eat
                    tree[i][j][k] += 1
            # 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 만약, 땅에 양분이 부족해

    return ground, tree, dead_tree


def summer(ground, dead_tree):
    while dead_tree:
        x, y, eat = dead_tree.pop()
        ground[x][y] += eat

    return ground


def autumn(tree):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(0, len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    # 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다. x][y]
                    for m in range(8):
                        next_x = i + dx[m]
                        next_y = j + dy[m]

                        if 1 <= next_x <= N and 1 <= next_y <= N:
                            tree[next_x][next_y].appendleft(1)

    return tree


def winter(ground, add):
    for i in range(N + 1):
        for j in range(N + 1):
            ground[i][j] += add[i][j]

    return ground


for i in range(K):
    ground, tree, dead_tree = spring(tree, ground)
    ground = summer(ground, dead_tree)
    tree = autumn(tree)
    ground = winter(ground, add)

total = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        total+=len(tree[i][j])

print(total)