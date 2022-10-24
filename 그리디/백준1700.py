N,K=map(int,input().split())
arr = list(map(int,input().split()))
stack=[]
for i in arr:
    stack.append(i)
stack=stack[::-1]
multi =[0 for i in range(K+1)]
ans=0
while stack:
    now= stack.pop()
    if sum(multi)<N: #멀티탭 다 안찬경우
        multi[now]=1
        continue
    else:
        if multi[now]==1: #멀티탭에 있는경우
            continue

        cnt=0
        result =[0 for i in range(K+1)]
        wait = stack[::-1]
        for i in wait:
            result[i]=1 #재사용되는것체크
        for i in range(1,K+1):
            if multi[i]==1 and result[i]==1: #현재 꽂힌 것 중 재사용되는것
                cnt+=1
        if cnt==0: #재사용되는것 x
            for i in range(1,K+1):
                if multi[i]==1: #현재 꽂힌 것 중 재사용되는것
                    multi[i]=0
                    break
        elif cnt<N: # 전부 재사용 X
            for i in range(1,K+1):
                if multi[i]==1 and result[i]==0: #재사용안되는것 빼기
                    multi[i]=0
                    break
        elif cnt==N: #전부재사용 -> 현재 시점에서 가장 나중에 사용되는것
            cn=0
            new=set()
            # print('wait',wait)
            for i in wait:
                if multi[i]==1 and result[i]==1 and i not in new: #재사용되는것중 가장 늦은 것
                    cn+=1
                    new.add(i)
                    if cn==N:
                        multi[i]=0
                        break
        ans+=1
        multi[now]=1
        # print('mult',multi)
        # print('ans',ans)
print(ans)