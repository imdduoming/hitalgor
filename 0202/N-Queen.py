total = 0
def solution(n):
    visited = [-1] * (n)
    back_tracking(0, n, visited)
    return total

def back_tracking(x, n, visited):
    global total
    print("x:",x,visited)

    if x == n :
        total += 1
        return
    for i in range(n):
        # print("절댓값:",abs(y-i))
        visited[x]=i
        flag=0
        if x==0:
            back_tracking(x+1,n,visited)
        else:
            for j in range(x):
                if visited[x] == visited[j] or abs(visited[x] - visited[j]) == (x - j):
                    flag=1
                    break

            if flag==0:
                back_tracking(x + 1, n, visited)


print(solution(5))