from collections import deque


def bfs(place, x, y, visited):
    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = True

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    check = True
    while queue:
        x, y, cost = queue.popleft()
        if cost == 2:
            continue
        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nx][ny]:
                    continue
                if place[nx][ny] == 'P':
                    return False
                if place[nx][ny] == 'O':
                    queue.append((nx, ny, cost + 1))
                    visited[nx][ny] = True
    return True


def solution(places):
    answer = []

    for place in places:
        # 거리두기 확인
        visited = [[False] * 5 for _ in range(5)]
        flag = True
        for j in range(0, 5):
            for k in range(0, 5):
                # P 이면 거리두기 확인
                if place[j][k] == 'P':
                    if not bfs(place, j, k, visited):
                        flag = False
                        break

        if not flag:
            answer.append(0)
        else:
            answer.append(1)
    return answer
