def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s

def solution(play_time, adv_time, logs):
    answer = 0
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)

    # 초로 환산된 play_time 의 size 만큼 모든 시간별 시청자수 저장
    time = [0 for i in range(play_time + 1)]
    for i in logs:
        start,end = i.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        time[start] +=1 # 누군가 시청 시작
        time[end] -=1 #누군가 시청 종료

    # 위에서 체크해둔 시작과 끝을 바탕으로 모든 구간에 시청자 수 기록
    for i in range(1,len(time)):
        time[i]= time[i]+time[i-1]

    # 누적값을 확인하기 위해 동일코드 반복 / time[i] 는 0~ i 초까지의 누적 시청자 수
    for i in range(1,len(time)):
        time[i]= time[i]+time[i-1]

    # 누적된 시청자 수를 바탕으로 가장 시청자 수가 많은 구간 탐색
    max_view =-1

    for i in range(adv_time-1,play_time):
        tmp = time[i] - time[i-adv_time]
        if tmp > max_view:
            max_view=tmp
            answer = i-adv_time+1

    return int_to_str(answer)


