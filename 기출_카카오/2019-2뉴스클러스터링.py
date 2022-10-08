def solution(str1, str2):
    import math
    answer = 0
    set1 =list()
    set2=list()
    for i in range(0,len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            word= str1[i].lower()+str1[i+1].lower()
            set1.append(word)
    print(set1)

    for i in range(0,len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            word= str2[i].lower()+str2[i+1].lower()
            set2.append(word)
    print(set2)

    if len(set1) > len(set2) :
        # 교집합 개수 구하기
        inter=[set1.remove(x) for x in set2 if x in set1]
    else :
        inter=[set2.remove(x) for x in set1 if x in set2]

    # 합집합은 교집합+나머지 원소들

    list_uni=set1+set2
    uni=len(list_uni)

    if uni == 0 :
        return 65536

    return int(len(inter)/uni*65536)
