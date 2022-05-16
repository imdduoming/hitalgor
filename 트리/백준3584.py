T = int(input())


def find_ancestor(num1, num2, tree):
    # num1의 부모들 찾기
    ans = 0
    root = 0
    parent1 = num1
    parent2 = num2

    # 부모가 아무도 없으면 루트임
    num1_parent = {parent1: 1}
    while True:
        if parent1 not in tree:
            break
        if parent1 in tree:
            parent1 = tree[parent1]
            num1_parent[parent1] = 1

    while True:
        if parent2 not in tree:
            ans = parent2
            break
        if parent2 in tree:
            if parent2 in num1_parent:
                ans = parent2
                break
            parent2 = tree[parent2]
    return ans


for i in range(T):
    N = int(input())
    tree = {}
    for j in range(N - 1):
        parent, child = map(int, input().split())
        if child not in tree:
            tree[child] = parent
    num1, num2 = map(int, input().split())

    ans = find_ancestor(num1, num2, tree)
    print(ans)
