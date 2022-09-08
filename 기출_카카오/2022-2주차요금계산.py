def solution(fees, records):
    answer = []
    car_info={}
    answer_dict={}
    res=0
    for i in records:
        time,num,info=i.split()
        minutes=60*int(time.split(':')[0])+int(time.split(':')[1])
        if info=='IN':
            car_info[num]=(0,minutes)
        else:
            res=minutes-car_info[num][1]
            car_info[num]=(1,res)
            if num not in answer_dict:
                answer_dict[num]=res
            else:
                answer_dict[num]+=res

    for i,v in car_info.items():
        if v[0]==0:
            minutes=23*60+59-v[1]
            if i not in answer_dict:
                answer_dict[i]=minutes
            else:
                answer_dict[i]+=minutes
    ans=0
    res=0

    for i,v in answer_dict.items():
        if v<=fees[0]:#기본시간보다 적으면
            ans=fees[1]
        else:
            ans=fees[1]
            if (v-fees[0])%fees[2]==0:
                res=(v-fees[0])//fees[2]
                ans+=res*fees[3]
            else:
                res=(v-fees[0])//fees[2]
                ans+=(res+1)*fees[3]

        answer_dict[i]=ans
    items=sorted(answer_dict.items(),key=lambda x:x[0])
    for i,j in items:
        answer.append(j)


    return answer
print(solution([1, 461, 1, 10],	["00:00 1234 IN"]))