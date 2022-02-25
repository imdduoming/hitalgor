from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 트럭은 1초에 한칸씩 이동

    total = 0
    bridge = [0] * bridge_length

    while bridge:
        answer += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                now = truck_weights.pop(0)
                bridge.append(now)
            else:
                bridge.append(0)

    return answer