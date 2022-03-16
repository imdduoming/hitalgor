def solution(n, clockwise):
    answer = [[0 for i in range(n)] for j in range(n)]
    cnt=n

    if clockwise==True: #시계방향

        num=1
        start=0
        start_1 = 0
        start_2 = 0
        start_3 = n-1
        start_4= n-1
        while cnt>=1:
            #1번
            now=num
            for i in range(start_1,cnt):
                answer[start][i]=now
                now= now+1
            start_1+=1
            #2번
            now = num
            for i in range(start_2, cnt):
                answer[i][n-1-start] = now
                now= now + 1
            start_2+=1
            print('2번',answer)
            # 3번
            now = num
            for i in range(start_3,start_3-cnt+1,-1):
                answer[n - 1 - start][i] = now
                now = now + 1
            start_3-=1
            print('3번', answer)
            # 4번
            now = num
            for i in range(start_4, start_4 - cnt + 1, -1):
                answer[i][start] = now
                now = now + 1
            print('4번', answer)
            num=now
            start_4-=1

            cnt-=2
            start+=1

        if n%2==1: #n이 홀 수 이면
            answer[n//2][n//2]=num
        print(answer)

    else:
        # 반시계
        cnt=cnt-1
        num = 1
        start = 0
        start_1 = 0
        start_2 = n-1
        start_3 = n-1
        start_4 = 0
        while cnt >= 1:
            # 1번
            now = num
            for i in range(start_1, cnt+start_1):
                answer[i][start] = now
                now = now + 1
            start_1 += 1

            # 2번
            now = num
            for i in range(start_2, start_2-cnt,-1):
                answer[start][i] = now
                now = now + 1
            start_2 -= 1

            # 3번
            now = num
            for i in range(start_3, start_3 - cnt , -1):
                answer[i][n-1-start] = now
                now = now + 1
            start_3 -= 1

            # 4번
            now = num
            print(start_4)
            for i in range(start_4, start_4+cnt):
                answer[n-1-start][i] = now
                now = now + 1
                print(answer)
                print('4번:',now)
            start_4 += 1


            num = now
            print('num',num)
            print(answer)
            cnt -= 2
            start += 1

        if n % 2 == 1:  # n이 홀 수 이면
            answer[n // 2][n // 2] = num
    return answer