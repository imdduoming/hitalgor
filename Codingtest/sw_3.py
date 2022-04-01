a,b=map(int,input().split())
t=input()
arr=[]

for i in t:
    num=(ord(i)-ord('a'))
    arr.append(num)
answer=[]
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in arr:
    cnt=1

    while ((26*cnt+i-b)%a) !=0:
        cnt+=1
    ans= ((26 * cnt + i - b) // a)% 26
    answer.append(ans)

for i in answer:
    print(alpha[i],end='')
