def solution(people, limit):
    from collections import deque
    answer = 1000000

    boat_cnt = 0
    people.sort()

    queue = deque(people)

    while queue:
        if len(queue) == 1:
            boat_cnt += 1
            break
        now = queue.pop()
        now_left = queue.popleft()
        boat_cnt += 1
        if limit - now < now_left:  # 두개가 보트에 탈 수 없는경우
            queue.appendleft(now_left)

    return boat_cnt

