# def solution(gems):
#     answer = []
#     org_dict={}
#     for i in gems:
#         if i not in org_dict:
#             org_dict[i] = 1
#     gems_type=len(set(gems))
#     dict={}
#     left=0
#     right=0
#     while right<len(gems):
#         if gems[right] not in dict:
#             dict[gems[right]]=1
#             if len(dict)==gems_type:
#                 break
#             else:
#                 right+=1
#         else:
#             dict[gems[right]]+=1
#             right+=1
#
#     while left<len(gems):
#         if len(dict)==gems_type:
#             dict[gems[left]]-=1
#             if dict[gems[left]]==0:
#                 break
#             else:
#                 left+=1
#
#     answer.append(left+1)
#     answer.append(right+1)
#     return answer
#
# print(solution(["A","B","B","B","B","B","B","C","B","A"]))