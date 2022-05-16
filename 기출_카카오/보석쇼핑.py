def solution(gems):
    answer = []
    org_dict={}
    for i in gems:
        if i not in org_dict:
            org_dict[i] = 1
    gems_type=len(org_dict)
    print(dict)
    left=0
    right=0
    while left<=right:
        if gems[right] not in dict:
            dict[gems[right]]=1
            if len(dict)==gems_type:
                left+=1
        else:
            dict[gems[right]] += 1
            right+=1







    return answer