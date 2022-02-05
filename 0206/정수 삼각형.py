def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        for j in range(0,len(triangle[i])):
            if j==0:
                triangle[i][j]=triangle[i-1][j]+triangle[i][j]
            elif j==(len(triangle[i])-1):
                triangle[i][j] = triangle[i - 1][j-1] + triangle[i][j]
            else:
                left=triangle[i - 1][j-1] + triangle[i][j]
                right=triangle[i][j]=triangle[i-1][j]+triangle[i][j]
                triangle[i][j]=max(left,right)
            print(triangle[i][j])
    last=len(triangle)-1


    for i in triangle[last]:
        answer=max(i,answer)
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))