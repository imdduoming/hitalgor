def solution(nodeinfo):
    answer = []
    new_node=[]
    global pre
    global post
    for i in range(len(nodeinfo)):
        new_node.append((i,nodeinfo[i][0],nodeinfo[i][1]))
    new_node.sort(key=lambda x: (-x[2],x[1]))
    # 레벨 지정 해주는 함수
    level_dict = level(new_node)
    print('level_dict',level_dict)
    Tree =[]
    Tree = make_tree(level_dict)
    bt = BinaryTree()
    bt.root= Tree[0]
    bt.preorder()
    bt.postorder()
    answer.append(pre)
    answer.append(post)
    return answer

class TreeNode(object):
    def __init__(self,x,num):
        self.left = None
        self.right = None
        self.x = x
        self.num = num
class BinaryTree(object):
    def __init__(self):
        self.root = None
    def preorder(self):
        def _preorder(node):
            pre.append(node.num+1)
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)
        _preorder(self.root)

    def postorder(self):
        def _postorder(node):
            if node.left:
                _postorder(node.left)
            if node.right:
                _postorder(node.right)
            post.append(node.num+1)
        _postorder(self.root)

def make_tree(level_dict):
    Tree = []
    node = TreeNode(level_dict[0][0][1],level_dict[0][0][0])
    root = node
    Tree.append(node)
    for i in range(1,len(level_dict)):
        for j in level_dict[i]:
            print('현재 x',j[1])
            print('현재 num',j[0])
            node = TreeNode(j[1],j[0])
            x = j[1]
            current = root
            while True :
                if x<current.x:
                    if current.left==None:
                        current.left = node
                        break
                    current=current.left
                else:
                    if current.right==None:
                        current.right = node
                        break
                    current=current.right
            Tree.append(node)
            print('현재 tree',Tree)

    print('Tree',Tree)
    return Tree

def level(new_node):
    level_dict=[]
    if len(new_node) ==1 :
        level_dict.append([new_node[0]])
    else:
        level_dict.append([new_node[0]])
        level_dict.append([new_node[1]])
        last = new_node[1][2]
        for i in range(2,len(new_node)):
            if new_node[i][2]==last:
                level_dict[-1].append(new_node[i])
            else:
                level_dict.append([new_node[i]])
            last= new_node[i][2]
    return level_dict

pre = []
post = []

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))