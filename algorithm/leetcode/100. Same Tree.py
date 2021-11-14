

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional
"""

100. Same Tree
input = two tree 
output = tree1 eq tree2 -> true

Constraints:

    The number of nodes in both trees is in the range [0, 100].
    -104 <= Node.val <= 104

DS - BFS

1. 두개의 트리를 큐에 넣는다.
2. 큐에서 꺼내서 두개의 트리를 비교하여 값이 다르고 동일한 위치에 있지 않으면 false
3. 모두 같으면 true

"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def bfs(p,q):
            ret = True
            que = deque()
            que.append((p,q))
            while que:
                node1,node2 = que.popleft()
                if not node1:
                    if node2:
                        ret = False
                        return ret
                    if not node2:
                        ret = True
                        return ret
                if node1:
                    if not node2:
                        ret = False
                        return ret
                if node1 and node2:
                    print("3")
                    if node1.val !=node2.val:
                        ret = False
                        return ret
                    if not node1.left:
                        if node2.left:
                            ret = False
                            return ret
                    if not node1.right:
                        if node2.right:
                            ret = False
                            return ret 
                if node1.left:
                    print("1")
                    if not node2.left:
                        ret = False
                        return ret
                if node1.right:
                    print("2")
                    if not node2.right:
                        ret = False
                        return ret
                if node1.left and node2.left:
                    print("3")
                    if node1.left.val != node2.left.val:
                        print("l틀림")
                        ret = False
                        return ret
                    que.append((node1.left, node2.left)) 
                if node1.right and node2.right:
                    if node1.right.val != node2.right.val:
                        print("r틀림")
                        ret = False
                        return ret
                    que.append((node1.right, node2.right))
            return ret
    
        return bfs(p,q)