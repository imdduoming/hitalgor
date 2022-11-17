# 백준 자료구조 구현 실버 1 괄호의 값
s=list(input())
res=1
stack=[]
result=0
for i in range(len(s)):
    if s[i]=='(':
        res*=2
        stack.append(s[i])
    elif s[i]=='[':
        res*=3
        stack.append(s[i])
    elif s[i]==')':
        if not stack or stack[-1]!='(':
            result=0
            break
        elif s[i-1]=='(':
            result+=res
        res=res//2
        stack.pop()
    elif s[i]==']':
        if not stack or stack[-1]!='[':
            result=0
            break
        elif s[i-1]=='[':
            result+=res
        res=res//3
        stack.pop()
if stack:
    print(0)
else:
    print(result)
