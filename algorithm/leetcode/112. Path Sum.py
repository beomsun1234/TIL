"""
112. Path Sum
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Input: 트리 , targetSum = 22
Output: 루트부터 리프까지 레벨이 같이 않는 노드들의 합이 targetSum과 같으면 true

Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000

time = o(n) 트리의 노드를 dfs를 통해 n (깊이 만큼) 확인하기에
space - o(n) 트리의 노드를 dfs를 통해 n만큼 스택에 저장해 놓고 사용하기에
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        global ret
        ret = False
        def dfs(root, nowSum, targetSum):
            global ret
            if not root:
                return
            nowSum += root.val
            if not root.left and not root.right:
                if nowSum == targetSum:
                    print(nowSum)
                    ret = True  
                    return ret
                else:
                    return ret
            if root.left:
                dfs(root.left,nowSum, targetSum)
            if root.right:
                dfs(root.right, nowSum, targetSum)
    
        dfs(root,0,targetSum)
        return ret
        