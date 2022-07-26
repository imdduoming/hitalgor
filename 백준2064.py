import sys
input=sys.stdin.readline
N=int(input())
addr=[]
for i in range(N):
    addr.append(input().rstrip().split('.'))
net_addr = []
net_mask = []
for i in range(4):
    min_ip = int(addr[0][i])
    max_ip = int(addr[0][i])
    for tmp_ip in addr:
        if max_ip < int(tmp_ip[i]):
            max_ip = int(tmp_ip[i])
        if min_ip > int(tmp_ip[i]):
            min_ip = int(tmp_ip[i])
    if 255 == 256 + (~max_ip^min_ip): # 모든 비트가 같다면
        net_mask.append(255)
    else: # 다른 비트를 찾았다면
        for j in range(9):
            if -(~max_ip^min_ip) <= 1<<j:
                net_mask.append(256 - (1<<j))
                for k in range(3):
                    net_mask.append(0)
                break
    net_addr.append(int(addr[0][i])&net_mask[i])
net_mask = net_mask[:4]
print("{}.{}.{}.{}".format(net_addr[0], net_addr[1], net_addr[2], net_addr[3]))
print("{}.{}.{}.{}".format(net_mask[0], net_mask[1], net_mask[2], net_mask[3]))
