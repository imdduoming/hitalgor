import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        first=heapq.heappop(scoville)
        if first>K:
            break
        else:
            answer+=1
            second=heapq.heappop(scoville)
            new=first+second*2
            heapq.heappush(scoville,new)

    return answer


print(solution([1, 2, 3, 9, 10, 12]	,7))