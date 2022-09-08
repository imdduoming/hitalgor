def solution(s):
    answer = []
    s=s[1:-1]
    s = s.split(',')
    dict={}
    for i in s:
        i=str(i)
        if i[0]=='{':
            i=i[1:]
        if i[-1]=='}':
           i=i[:-1]
        i=int(i)
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1


    sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)

    for i,j in sorted_dict:
        i=int(i)
        answer.append(i)

    return answer

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))