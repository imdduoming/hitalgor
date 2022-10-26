from itertools import combinations
n=int(input())
answer=[]
for i in range(1,11):
    for j in combinations(range(10),i):
        nums=sorted(list(j),reverse=True)
        answer.append(int("".join(map(str, nums))))

answer.sort()
if n>=len(answer):
    print(-1)
else:
    print(answer[n])








