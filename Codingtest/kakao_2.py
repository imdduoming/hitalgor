def solution(queue1, queue2):
    answer = -2
    from collections import deque
    len_q=len(queue1)
    total=sum(queue1)+sum(queue2)
    check_flag=0

    q=queue1+queue2
    if max(q)>sum(q)-max(q):
        check_flag=1

    queue1=deque(queue1)
    queue2=deque(queue2)
    cnt=0

    if check_flag==1:
        answer=-1
    else:
        while True:
            if total%2==0:
                if sum(queue1)==total//2:
                    break
            if sum(queue1)<sum(queue2):
                queue1.append(queue2.popleft())
                cnt+=1
            elif sum(queue1)>sum(queue2):
                queue2.append(queue1.popleft())
                cnt+=1
        answer=cnt
    return answer


print(solution([4, 5], [9, 1]))