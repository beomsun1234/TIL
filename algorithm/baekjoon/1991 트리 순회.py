"""
1991 트리 순회
"""

class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right




N = int(input())
tree = {}

for _ in range(N):
    node, left, right = map(str, input().split())
    tree[node] = Node(item=node, left=left, right=right)

def preorder(node): # root , left, right
    print(node.item, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node): # l, root, r
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end='')
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node): # left, right, root
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end='')



# 항상 A가 루트다
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])