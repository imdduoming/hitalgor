from collections import deque

def solution(skill, skill_trees):
    answer = 0
    skill_dict = {}

    for i in skill:
        if i not in skill_dict:
            skill_dict[i] = 1
    for i in skill_trees:
        queue = deque(skill)

        flag=True
        for j in i:
            # print('j:',j)
            if queue and j in skill_dict:
                now = queue.popleft()
                # print('j:',j,'now:',now)
                if now!=j:
                    flag=False
                    break
        if flag==True:
            answer+=1
        # print(new_queue)
    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))