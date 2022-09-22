# 백준 거북이
# 실버 3
T = int(input())
def size_box(queue):
    x_queue=sorted(queue,key=lambda x:x[0])
    max_x=x_queue[-1][0]
    min_x=x_queue[0][0]
    y_queue=sorted(queue,key=lambda x:x[1])
    max_y=y_queue[-1][1]
    min_y=y_queue[0][1]
    # print(max_x,max_y,min_x,min_y)
    if min_x==max_x or max_y==min_y:
        return 0
    else:
        # print((max_x-(min_x)) * (max_y-(min_y)))
        return (max_x-(min_x)) * (max_y-(min_y))
for i in range(T):
    x,y=0,0
    queue=[]
    command = input()
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    dir=0
    queue.append((0,0))
    for c in command:
        if c=='F':
            x,y=x+dx[dir],y+dy[dir]
            queue.append((x,y))
        elif c=='B':
            x,y=x-dx[dir],y-dy[dir]
            queue.append((x,y))
        elif c=='L':
            dir=(dir-1)%4
        else:
            dir=(dir+1)%4
    print(size_box(queue))


