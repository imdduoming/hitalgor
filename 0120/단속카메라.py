def solution(routes):
    answer = 1
    routes.sort(key=lambda x:(x[1],x[0]))
    loc=routes[0][1]
    for i in range(1,len(routes)):
        if loc<routes[i][0]:
            answer+=1
            loc=routes[i][1]
    return answer


print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))