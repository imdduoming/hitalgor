
def solution(today, terms, privacies):
    answer = []
    dict={}
    for i in terms:
        term,period=i.split()
        if term not in dict:
            dict[term]=int(period)

    for i in range(0,len(privacies)):
        when,term = privacies[i].split()
        period = dict[term]
        year, month ,day = when.split('.')
        int_year ,int_month ,int_day = int(year),int(month),int(day)
        due=''
        if period+int_month>12:
            int_year += (period+int_month)//12
            if (period+int_month)%12==0:
                int_month=((period+int_month)%12)+1
            else:
                int_month=(period+int_month)%12
        else:
            int_month += period
        today=today.replace('.','')

        if int_day==1:
            int_month= int_month-1
            if int_month==0:
                int_month=12
                int_year-=1
            int_day = 28
        else:
            int_day-=1

        if int_month<10:
            month='0'+str(int_month)
        else:
            month=str(int_month)

        if int_day<10:
            day = '0'+str(int_day)
        else:
            day= str(int_day)
        due=str(int_year)+month+day
        if today>due:
            answer.append(i+1)
    print(due)
    print(today)
    return answer


print(solution("2020.09.01",["A 5"],["2022.08.02 A"]))