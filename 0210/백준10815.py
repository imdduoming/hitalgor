#숫자카드 실버4
N=int(input())
card=list(map(int,input().split()))
M=int(input())
answer=[]
dict={}
test=list(map(int,input().split()))
for i in card:
    if i not in dict:
       dict[i]=1


for i in test:
    if i not in dict:
        answer.append(0)
    else:
        answer.append(1)
for i in answer:\
    print(i,end=' ')
