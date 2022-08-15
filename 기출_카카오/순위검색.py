def solution(infos, query):
    answer = []
    dict= {}
    scores =[]
    c1=[]
    for lang in ['cpp', 'java', 'python', "-"]:
        for job in ['backend', 'frontend', "-"]:
            for career in ['junior', 'senior', "-"]:
                for food in ['chicken', 'pizza', "-"]:
                    dict[lang + job + career + food] = []

    for info in infos:
        info = info.split(" ")
        for lang in [info[0], "-"]:
            for job in [info[1], "-"]:
                for career in [info[2], "-"]:
                    for food in [info[3], "-"]:
                        dict[lang + job + career + food].append(int(info[4]))

    for i in query:
        list= i.replace(' and ','')
        i_query=list.split()
        i_score=int(i_query[1])
        i_query=i_query[0]

        # 알맞은 조건문을 작은 점수 순으로 정렬
        info_score= sorted(dict[i_query])
        # print(info_score)
        leng = len(info_score)
        tmp = leng

        low=0
        high =leng-1

        while low <= high:
            mid = (low + high) // 2

            if i_score <= info_score[mid]:
                tmp = mid
                high = mid - 1

            else:
                low = mid + 1

        answer.append(leng-tmp)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))