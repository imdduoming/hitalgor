from typing import List
def solve(num):
    cnt=1
    while True:
        if cnt>=num:
            num=cnt
            break
        else:
            cnt=cnt*2
    return num
def solution(queries: List[List[int]]) -> int:
    answer = 0
    dict= {}
    for i,j in queries:
        if i not in dict:
            dict[i]=[0,0]

        if j+dict[i][1] <= dict[i][0]:
            # 원소수 <=배열크기
            dict[i][1]+=j
        else:
            answer+=dict[i][1]
            new_size= solve(dict[i][1]+j)
            dict[i][0]=new_size
            dict[i][1]=dict[i][1]+j

    return answer

print(solution([[1,1]]))