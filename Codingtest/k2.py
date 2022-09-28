def solve(users,prices,emoticons):
    total_money=0
    total_plus=0
    for i in users:
        can_buy=i[0]
        user_money=i[1]
        money=0
        plus_flag=False
        for j in range(0,len(prices)):
            if can_buy<=prices[j]:
                money+=emoticons[j]*((100-prices[j])/100)
                money=int(money)

                if money>=user_money:
                    plus_flag=True
                    break

        if plus_flag==True:
            total_plus+=1

        else:
            total_money+=money

    print('최종','total_plus',total_plus,'total_money',total_money)
    return total_plus,total_money



def solution(users, emoticons):
    from itertools import product
    answer = []
    discounts=[10,20,30,40]

    data = list(product(discounts, repeat = len(emoticons)))
    for i in range(0,len(data)):
        print(data[i])
        total_plus,total_money=solve(users,data[i],emoticons)
        answer.append((total_plus,total_money))
        print(answer)
    answer.sort(reverse=True,key=lambda x:(x[0],x[1]))
    return answer[0]
print(solution([[40,2900],[23,10000],[11,5200],[5,5900],[40,3100],[27,9200],[32,6900]],[1300,1500,1600,4900]))