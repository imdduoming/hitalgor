def solution(p):
    answer = ''
    stack = []

    if check_right(p) or p == '':
        return p
    else:  # 문자열이 올바른 문자열이 아니라면 알고리즘 시작
        return algor(p,'')


def algor(p,total):
    if p=='':
        # print('빈문자열')
        return ''
    else:
        # u,v로 분리
        right = 0
        left = 0
        u = ''
        v = ''
        idx = 0
        for i in range(len(p)):
            if p[i] == '(':
                left += 1
            else:
                right += 1
            u += p[i]
            if left == right:
                idx = i
                break
        #v 분리과정
        if p[i + 1:]:
            v=p[i + 1:]
        else:
            v=''

        # print('u:',u,'v:',v)
        if check_right(u):  # u가 올바른 괄호 문자열일 경우
            return u+algor(v,total)
        else:
            total += '('
            total += algor(v,total)
            total += ')'
            for i in range(0, len(u)):
                if i == 0 or i == (len(u) - 1):
                    continue
                else:
                    if u[i] == '(':
                        total += ')'
                    else:
                        total += '('
            # print(total)
            return total


def check_right(str):
    # 문자열이 올바른 문자열인지 판별하는 함수
    stack = []
    for i in str:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    else:
        return True

    return answer

solution("()))((()")