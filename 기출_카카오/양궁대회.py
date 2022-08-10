#2022 블라인드
def solution(n, info):
    answer = [-1]
    from itertools import combinations_with_replacement
    diff=0
    ans=0
    k=0
    for score in combinations_with_replacement(range(11),n):
        k+=1
        info_lion=[0]*11
        score_l=0
        score_a=0
        for sel in score:
            info_lion[10-sel]+=1
        for i in range(10,-1,-1):
            if info_lion[i]>info[i]:
                score_l+=10-i
            elif info_lion[i]==info[i]:
                if info_lion[i]==0:
                    continue
                else:
                    score_a+=10-i
            else:
                score_a+=10-i

        if score_l>score_a:
            diff=score_l-score_a # 점수차
            if diff>ans:
                ans=diff
                answer=info_lion

    return k

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))