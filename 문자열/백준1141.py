#접두사 실버 2
# 접두사가 아닌 것을 카운트
N=int(input())
words=[]
for i in range(N):
    words.append(input().rstrip())

words.sort(key=lambda x:len(x))
cnt=0
for i in range(0,len(words)):
    flag=False
    for j in range(i+1,len(words)):
        if words[j].startswith(words[i]):
            flag=True
    if flag==False:
        cnt+=1

print(cnt)