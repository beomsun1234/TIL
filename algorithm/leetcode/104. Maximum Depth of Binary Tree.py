"""
    104. Maximum Depth of Binary Tree
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path from the root node down         to the farthest leaf node.
    가장 멀리있는 리프노드의 레벨을 반환해라
    
    input = tree
    output = tree depth int형
    onstraints:

    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
    
    DS - bfs
    
    1. 큐에  root와 level을 함께 넣는다.
    2. 큐를 빼서 node의 왼쪽 오른쪽을 검사한다.
    3. 자식이 존재하면 큐에 자식을 넣는다.
    4. 모두 확인하여 level을 반환한다.
"""
from collections import deque
from typing import Optional
class Solution:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        d = 0
        q = deque()
        q.append((root,d))
        while q:
            node, ret = q.popleft()
            if not node:
                return 0
            if node.left:
                q.append((node.left,ret+1))
            if node.right:
                q.append((node.right,ret+1))

        print(ret+1)
        return ret+1
        
        