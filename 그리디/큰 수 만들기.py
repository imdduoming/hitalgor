#그리디
def solution(number, k):
    answer = ''
    stack = []
    cnt = 0
    flag=0
    for num in number:
        if not stack:
            stack.append(num)
        else:
            if num>=stack[-1]:
                while stack and num>stack[-1]:
                    stack.pop()
                    cnt+=1
                    if cnt==k:
                        flag=1
                        break
                stack.append(num)
            else:
                cnt+=1

        if flag==1 or cnt==k:
            break
    if stack:
        answer
print(solution("4177252841"	,4))