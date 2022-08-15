def solution(gems):
    import sys
    answer = [1,len(gems)]
    org_dict={}
    for i in gems:
        if i not in org_dict:
            org_dict[i] = 1
    gems_type=len(set(gems))
    dict={}
    left=0
    right=0
    ans=sys.maxsize
    dict[gems[0]]=1
    while right<len(gems):
        if len(dict)<gems_type:
            right+=1
            # print('right',right)
            if right<len(gems):
                if (gems[right] not in dict) :
                    dict[gems[right]]=1

                else:
                    dict[gems[right]]+=1


        else:
            if answer[1]-answer[0]>right-left:
                answer=[left+1,right+1]
                # print(answer)
            if dict[gems[left]]==1:
                del dict[gems[left]]
            else:
                dict[gems[left]]-=1
            left+=1
            # print('left',left)
        # print(dict)

    return answer

print(solution(["A","B","B","B","B","B","B","C","B","A"]))