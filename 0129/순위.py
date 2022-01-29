# 플루이드 워셜 알고리즘
def solution(n, results):
    answer=0
    matrix = [[None for _ in range(n)] for _ in range(n)]
    for win, lose in results:
        matrix[win][lose] = True
        matrix[lose][win] = False

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                #자기자신이 아니면서 아직 승패여부를 모른다면
                if a!=b and matrix[a][b]!=None:
                    #a도 k를 이기고 k도  b를 이겼다면
                    if matrix[a][k]==True and matrix[k][b]==True:
                        matrix[a][b]=True
                        # a도 k에게 지고 k도  b에게 졌다면
                    elif matrix[a][k]==False and matrix[k][b]==False:
                        matrix[a][b]=False

    for i in range(1,n+1):
        #승패여부를 알 수 없는 것이 자기자신밖에 없다면
        if matrix[i][1:].count(None)==1:
            answer+=1

    return answer