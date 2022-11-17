# 실버 3 사탕게임
N=int(input())
candy=[]
for i in range(N):
   arr=list(input())
   candy.append(arr)

max_cnt=0
def get_max(flag,another,one,two):
    global max_cnt
    global candy
    if flag==0: #세로 확인
        # 그 줄 가로 확인
        first=candy[another][0]
        cnt=1
        m=0
        for i in range(1,N):
            if first==candy[another][i]:
                cnt+=1
            else:
                m=max(cnt,m)
                first=candy[another][i]
                cnt=1

        m=max(cnt,m)
        max_cnt=max(m,max_cnt)

        first=candy[0][one]
        cnt=1
        m=0
        for i in range(1,N):
            if first==candy[i][one]:
                cnt+=1
            else:
                m=max(cnt,m)
                first=candy[i][one]
                cnt=1
        m=max(cnt,m)
        max_cnt=max(m,max_cnt)

        first=candy[0][two]
        cnt=1
        m=0
        for i in range(1,N):
            if first==candy[i][two]:
                cnt+=1
            else:
                m=max(cnt,m)
                first=candy[i][two]
                cnt=1
        m=max(cnt,m)
        max_cnt=max(m,max_cnt)
    else:
        #가로바꾸기 그 해당 세로줄 확인
        first=candy[0][another]
        cnt=1
        m=0
        for i in range(1,N):
            if first==candy[i][another]:
                cnt+=1
            else:
                m=max(cnt,m)
                first=candy[i][another]
                cnt=1
        m=max(cnt,m)
        max_cnt=max(m,max_cnt)

        first=candy[one][0]
        cnt=1
        m=0
        for i in range(1,N):
            if first==candy[one][i]:
                cnt+=1
            else:
                m=max(cnt,m)
                first=candy[one][i]
                cnt=1
        m=max(cnt,m)
        max_cnt=max(m,max_cnt)

        first=candy[two][0]
        cnt=1
        m=0
        for i in range(1,N):
            if first==candy[two][i]:
                cnt+=1
            else:
                m=max(cnt,m)
                first=candy[two][i]
                cnt=1
        m=max(cnt,m)
        max_cnt=max(m,max_cnt)



def select():
    #가로 열 바꾸기
    global candy
    global max_cnt
    for i in range(N):
        for j in range(N-1):
            candy[i][j],candy[i][j+1]=candy[i][j+1],candy[i][j] #swapping
            get_max(0,i,j,j+1)
            # print('세로바꾸기',i,j,j+1,max_cnt)
            candy[i][j],candy[i][j+1]=candy[i][j+1],candy[i][j] #원래대로
    for j in range(0,N):
        for i in range(0,N-1):
            candy[i][j],candy[i+1][j]=candy[i+1][j],candy[i][j] #swapping
            get_max(1,j,i,i+1)
            # print('가로바꾸기',candy,j,i,i+1,max_cnt)
            candy[i][j],candy[i+1][j]=candy[i+1][j],candy[i][j] #swapping


select()
print(max_cnt)