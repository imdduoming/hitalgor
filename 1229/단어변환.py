def solution(begin, target, words):
    from collections import deque
    answer = 0
    queue = deque([begin])
    find = 0
    visited = {} #방문처리할 딕셔너리

    if target not in words: #target이 words에 없는 경우
        return 0

    while True:
        for i in range(0, len(queue)): #한 단계씩 BFS
            now = queue.popleft()

            if now == target: #이번 단계에서 찾을 경우
                find = 1
                return answer

            for word in words:
                if word not in visited: #방문하지 않은 단어만 조회
                    diff = 0 #다른 문자열 갯수 세기
                    for j in range(0, len(now)):
                        # 문자열 비교
                        if now[j] != word[j]:
                            diff += 1
                        # 문자열 다른 횟수가 1회 초과 => 다음 문자열이 될 수 없음 => 이문자는 더이상 조히하지 않아도됨
                        if diff > 1:
                            break
                    if diff == 1:  # 한 문자만 다르므로 다음문자 될 수 있음
                        queue.append(word) # 가지치기 할 queue에 단어 추가
                        visited[word] = 1  # 다음문자가 된 경우는 방문처리
        # 단계가 지날 때 마다 변환 횟수 1 추가
        answer += 1
    #다 돌아도 없는 경우는 0
    return 0