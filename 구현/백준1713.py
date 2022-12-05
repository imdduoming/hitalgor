#실버1 후보추천하기
N=int(input())
total=int(input())
candidates=list(map(int,input().split()))
dict={}
for candidate in candidates:
    if candidate in dict: # 틀에 있는 경우
        dict[candidate]+=1
    else:#틀에 없는 경우 추가해야함
        cnt=len(dict.keys())
        if cnt==N: #틀 꽉찬 경우
            min_val=min(dict.values())
            num=0
            for key in dict:
                if dict[key]==min_val: #가장 작은 값 영러개인지 찾기
                    num+=1
                    if num==2:#가장작은값 2개 이상
                        dict[last_key]=0 # 오래된 것 삭제
                        break
                    last_key=key

            del dict[last_key]
            # print('삭제 후',dict)
            dict[candidate]=1

        else:
            dict[candidate]=1
    # print(dict)

for i in sorted(dict.keys()):
    print(i,end=' ')
print()