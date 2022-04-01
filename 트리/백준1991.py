#트리순회
#백준 실버1
import sys
input=sys.stdin.readline
N=int(input())
tree={}
for i in range(0,N):
   a,b,c = input().split()
   tree[a]=[b,c]


print(tree)

def pre(root):
    if root!='.':
        print(root,end='')
        pre(tree[root][0])
        pre(tree[root][1])

def inorder(root):
    if root!='.':
        inorder(tree[root][0])
        print(root,end='')
        inorder(tree[root][1])

def post(root):
    if root!='.':
        post(tree[root][0])
        post(tree[root][1])
        print(root, end='')

pre('A')
print()
inorder('A')
print()
post('A')