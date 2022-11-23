#백준 1922 네트워크 연결 골드4
N=int(input())
M=int(input())

network=[]
for i in range(M):
    a,b,c=map(int,input().split())
    network.append((a,b,c))
#비용작은순대로 정렬
total=0
network.sort(key=lambda x:x[2])
# 특정 원소가 속한 집합을 찾기
def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find(parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [0] * (N + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, N + 1):
    parent[i] = i
MST=[]
for one,two,money in network:
    if find(one)!=find(two): #서로 다른 집합일 경우 합치기
        union(one,two)
        total+=money
        MST.append((one,two))


print(total)






