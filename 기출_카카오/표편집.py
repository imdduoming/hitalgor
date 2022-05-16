def solution(n, k, cmd):
    org_list={}
    remove_list=[]
    class Node:
        def __init__(self, data, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

    def make_table(n):
        prev_node = None
        root_node = None
        for i in range(n):
            if i == 0:
                node = Node(i)
                root_node = node
                prev_node = node
            else:
                node = Node(i)
                prev_node.next = node
                node.prev = prev_node
                prev_node = node

        return root_node

    #맨앞에 끼워넣기
    def start(k,root_node):
        for i in range(k):
            root_node=root_node.next

        return root_node

    def move_down(k, node):
        for i in range(k):
            node = node.next

        return node

    def move_up(k, node):
        for i in range(k):
            node = node.prev

        return node

    def delete(node):
        if node.next==None:
            node=node.prev
            node.next=None
        else:
            if node.prev is not None:
            #지우려는노드가 첫번째 노드가 아니면
                node.prev.next=node.next
            node.next.prev=node.prev
            node=node.next
        return node
        #지웠을 때의 idx 지운 배열에 추가

    def restore(node):
        prev_node=node.prev
        next_node=node.next
        if prev_node is not None:
            prev_node.next = node
        if next_node is not None:
            next_node.prev = node

    # 초기 링크드 리스트 생성

    root_node=make_table(n)
    now_node=start(k,root_node)
    print(now_node.data)
    for i in range(n):
        org_list[i]='O'

    for i in cmd:
        command=i.split()[0]
        # print(command)
        # print('현재 데이터:',now_node.data)
        #명령
        if command=='D':
            idx = int(i.split()[1])
            now_node=move_down(idx,now_node)

        elif command=='U':
            idx = int(i.split()[1])
            now_node=move_up(idx,now_node)

        elif command=='C':
            #삭제
            org_list[now_node.data] = 'X'
            remove_list.append(now_node)
            now_node=delete(now_node)


            #, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.


        elif command == 'Z':
            #z_data 는 원래 행 , z_idx 는 지워졌을 때의 행
            store_node=remove_list.pop()
            # print('복구할 데이터',store_node.data)
            org_list[store_node.data] = 'O'
            restore(store_node)


        # print(org_list)
    answer = ''.join(org_list.values())
    return answer

solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])