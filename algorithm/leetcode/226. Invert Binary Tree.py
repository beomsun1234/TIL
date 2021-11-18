
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional
"""
226. Invert Binary Tree
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tmp = Optional[TreeNode]
        
        if not root:
            return root
        
        q = deque()
        q.append((root, 1))
        
        while q:
            node, level = q.popleft()
            if node.right:
                q.append((node.right,level+1))
            if node.left:
                q.append((node.left, level+1))
            tmp = node.left
            node.left = node.right
            node.right = tmp
            
        return root
        
        