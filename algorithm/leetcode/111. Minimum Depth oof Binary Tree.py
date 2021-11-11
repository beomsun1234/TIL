"""
    111. Minimum Depth of Binary Tree

    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

    Note: A leaf is a node with no children.

    Input: root = [3,9,20,null,null,15,7]
    Output: 2

    Constraints:
        The number of nodes in the tree is in the range [0, 105].
        -1000 <= Node.val <= 1000

    DS - BFS
    트리의 level을 찾는 문제기에 BFS 선택 (BFS-> level by level)
    1. 처음 node(root)를 큐에 넣는다
    2. left와 right를 동 레벨로 두기위해 큐의 사이즈 만큼 반복문을 돌려준다. 
    3. 큐에서 node를꺼내서 left, right 검사 후 있으면 큐에 넣는다.
    4. 이 과정을 큐가 빌 때까지 반복하고 레벨을 증가시켜준다. 
    5. 큐에서 꺼낸 node의 left와 right 모두 없으면 리턴 현재 레벨+1 후 리턴 시킨다
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
# 
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def bfs(root):
            ck = 0
            if not root:
                return ck
            q = deque([root])
            print(len(q))
            while q:
                for i in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    if not node.left and not node.right:
                        ck+=1
                        print(ck)
                        return ck
                ck+=1
            return ck
        return bfs(root)
            
