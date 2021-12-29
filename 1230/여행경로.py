def solution(tickets):
    answer = []
    visited = {}  # 방문처리 배열
    stack = []
    for i in range(0, len(tickets)):
        start = tickets[i][0]
        end = tickets[i][1]
        if start not in visited:
            visited[start] = []
        visited[start].append(end)

    for a, b in visited.items():
        visited[a].sort(reverse=True)

    stack.append('ICN')
    path = []  # 경로 스택

    while stack:
        top = stack[-1]

        if top not in visited or len(visited[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(visited[top][-1])
            visited[top].pop()

    return path[::-1]




# def solution(tickets):
#     answer = []
#     visited = {}  # 방문처리 배열
#     stack = []
#     for i in range(0, len(tickets)):
#         start = tickets[i][0]
#         end = tickets[i][1]
#         if start not in visited:
#             visited[start] = []
#         visited[start].append(end)
#     # 방문처리 딕셔너리 출발지 - 도착지 딕셔너리
#     print(visited)
#     answer.append('ICN')
#     dfs('ICN', visited, answer)
#     return answer
#
#
# def dfs(start, visited, answer):
#     if start not in visited or len(visited[start]) == 0:
#         return
#     else:
#         arrive = visited[start]
#         arrive.sort(reverse=True)
#         while arrive:
#             # 도착지가 한 개 남아있는 경우에는 그 곳으로 결정
#             if len(arrive) == 1:
#                 new_start = arrive.pop()
#                 answer.append(new_start)
#                 dfs(new_start, visited, answer)
#
#             else:
#                 new_start = arrive.pop()
#                 # 다음 도착지의 도착지가 존재하여 다음 도착지로 가는 경우
#                 if len(visited[new_start]) != 0:
#                     answer.append(new_start)
#                     dfs(new_start, visited, answer)
#                 else:  # 알파벳 순이 아닌 다른 도착지로 결정
#                     second_start = arrive.pop()
#                     answer.append(second_start)
#                     visited[start].append(new_start)
#                     dfs(second_start, visited,
#
#
