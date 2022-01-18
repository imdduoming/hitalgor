from collections import deque
def solution(n, costs):
    answer = 0
    costs=sorted(costs,key=lambda x:x[2])
    connect=set([costs[0][0]])
    while len(connect)!=n:
        for i in range(0,len(costs)):
            if costs[i][0] in connect and costs[i][1] in connect:
                continue
            if costs[i][0] in connect or costs[i][1] in connect:
                answer+=costs[i][2]
                connect.update([costs[0][0],costs[0][1]])

    return answer