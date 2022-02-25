#프로그래머스 해시 LV2


def solution(clothes):
    answer = 0
    dict={}
    for name,type in clothes:
        if type not in dict:
            dict[type]=1
        else:
            dict[type] +=1

    answer=1
    for i in dict.values():
        answer*=(i+1)

    return answer-1