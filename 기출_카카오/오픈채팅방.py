#2019 카카오 블라인드 채용테스트

def solution(record):
    answer = []
    dict={}
    for i in record:
        if i[0]=='E' or i[0]=='C':
            command,id,nickname=i.split()
            dict[id]=nickname
    for i in record:
        print(i)
        if i[0]=='E':
            result=''
            command,id,nickname=i.split()
            result=dict[id]+'님이 들어왔습니다.'
            answer.append(result)

        elif i[0]=='L':
            result=''
            command, id = i.split()
            result = dict[id] + '님이 나갔습니다.'
            answer.append(result)

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))