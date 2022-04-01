def solution(money,costs):
    answer = 0
    value=[]
    for i in range(6):
        if i==0:
            value.append((costs[i]/1,1,costs[i]))
        elif i==1:
            value.append((costs[i]/5,5,costs[i]))
        elif i==2:
            value.append((costs[i]/10,10,costs[i]))
        elif i==3:
            value.append((costs[i]/50,50,costs[i]))
        elif i==4:
            value.append((costs[i]/100,100,costs[i]))
        else:
            value.append((costs[i]/500,500,costs[i]))

    value.sort(key=lambda x:x[0])
    idx=0
    total=0
    while True:
        if money==0:
            break
        cnt=money//value[idx][1]
        total+=cnt*value[idx][2]
        money-=value[idx][1]*cnt
        idx+=1
    print(total)

solution(1999	,[2, 11, 20, 100, 200, 600])


