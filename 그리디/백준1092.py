N=int(input())
crains=list(map(int,input().split()))
M=int(input())
box=list(map(int,input().split()))
crains.sort()
box.sort()

minute=1
box_cnt = len(box)
remain=[]
new_crain = crains[:]
if crains[-1] < box[-1]:
    print(-1)
else:
    while True:
        now_c = new_crain.pop()
        now_b = box.pop()
        if now_b<=now_c:
            box_cnt-=1
        else:
            new_crain.append(now_c)
            remain.append(now_b)
        if box_cnt==0:
            print(minute)
            break
        if len(new_crain)==0 or len(box)==0: #다음 트레인으로 옮겨야함
            minute+=1
            new_crain=crains[:]
            box = box+remain
            box.sort()
            remain=[]




