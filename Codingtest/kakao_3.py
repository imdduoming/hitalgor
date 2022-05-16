
def solution(alp, cop, problems):
    answer = 0
    cost=0

    now_alp = alp
    now_cop = cop

    for i in problems:
        if alp>= i[0] and cop>=i[1]:
            continue
        else:
            alp,cop,cost=solve(problems,alp,cop,i[0],i[1],cost)
            print('solve 함수 끝나고 현재력',alp,cop,cost)


    return answer
def solve(problems,now_alp,now_cop , need_alp, need_cop,cost):
    flag = 0

    print('현재 now',now_alp,now_cop)

    candidate = []
    if need_alp==now_alp:
        #코딩력만 필요
        need_more=1
    elif now_cop==need_cop:
        need_more=2
    elif max(need_alp, need_cop) == need_alp:
        need_more = 3
    elif max(need_alp, need_cop) == need_cop:
        need_more = 4

    print('need_more',need_more)
    for i in range(0, len(problems)):
        # 문풀 가능한 경우
        if now_alp >= problems[i][0] and now_cop >= problems[i][1]:
            s2_alp_cost = problems[i][2] / problems[i][4]
            s2_cop_cost = problems[i][3] / problems[i][4]
            total_cost=problems[i][4]
            candidate.append((i, s2_alp_cost, s2_cop_cost,total_cost))

        # 방법1의 경우

    candidate.append((-1,1,0,1))
    candidate.append((-1,0,1,1))


    if need_more==3:
        candidate.sort(reverse=True,key=lambda x:(x[1]+x[2],x[1]))
    elif need_more==4:
        candidate.sort(reverse=True, key=lambda x: (x[2]+x[1],x[2]))
    elif need_more == 1:
        #코딩력
        candidate.sort(reverse=True, key=lambda x: (x[2],x[2]+x[1]))
    elif need_more == 2:
        candidate.sort(reverse=True, key=lambda x: (x[1] ,x[1]+x[2]))

    print(candidate)

    need_idx = candidate[0][0]
    print('need_idx', need_idx)
    if need_idx!=-1:
        now_alp += problems[need_idx][2]
        now_cop += problems[need_idx][3]
        cost += problems[need_idx][4]
    else:
        # 방법1의 경우 갱신
        if need_more==1:
            cost += need_cop - now_cop
            now_cop+=(need_cop-now_cop)
            cost+=need_cop-now_cop
        else:
            cost += need_alp - now_alp
            now_alp+=(need_alp-now_alp)


    print('현재',now_alp,now_cop ,need_alp,need_cop)
    print('현재비용', cost)

    if now_alp >= need_alp and now_cop >= need_cop:
        return now_alp, now_cop,cost
    else:
        now_alp,now_cop,cost=solve(problems, now_alp,now_cop,need_alp, need_cop,cost)
    return now_alp,now_cop,cost



print(solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))