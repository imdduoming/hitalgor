def solution(survey, choices):
    answer = ''
    dict={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    type=["RT", "CF", "JM", "AN"]

    for i in range(0,len(survey)):
        res=choices[i]
        if res<4:
            select=survey[i][0]
            if res==1:
                dict[select]+=3
            elif res==2:
                dict[select] += 2
            elif res==3:
                dict[select] += 1
        elif res>4:
            select = survey[i][1]
            if res == 5:
                dict[select] += 1
            elif res == 6:
                dict[select] += 2
            elif res == 7:
                dict[select] += 3
    print(dict)

    for i in type:
        c1=i[0]
        c2=i[1]
        if dict[c1]<dict[c2]:
            answer+=c2
        else:
            answer += c1

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))