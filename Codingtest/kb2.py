def solution(money, minratio, maxratio, ranksize, threshold, months):
    answer = -1
    if maxratio==0 or money==0:
        return money
    if money<threshold:
        return money
    for i in range(months):
        #백의자리미만버림
        if money>=100:
            new_money=str(money)
            new_money=int(new_money[:-2]+'00')
            # print('버림',new_money)
        elif 10<=money<100: #십의자리는 일의자리 버리기
            new_money=str(money)
            new_money=int(new_money[:-1]+'0')
        else:
            new_money=int(money)

        if new_money<threshold:
            #세금걷지 않음
            break
        else:
            remain=new_money-threshold
            if remain<ranksize:
                rate=minratio
            else:
                ans=remain//ranksize
                rate=minratio+ans
                if rate>maxratio:
                    rate=maxratio
            tax=int(new_money*(rate/100))
            print('tax',tax)
            money-=tax
            money=int(money)
            print('rate',rate)
            print('money',money)
    return money