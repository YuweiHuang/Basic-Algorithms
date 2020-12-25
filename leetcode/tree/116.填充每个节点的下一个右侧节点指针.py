#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Node(object):
    """
    docstring
    """
    def __init__(self, val = 0, left = None, right = None, next = None):
        """
        docstring
        """
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def _connectTwo(self, node1: 'Node', node2: 'Node'):
        """
        docstring
        """
        if node1 == None or node2 == None:
            return
        node1.next = node2
        self._connectTwo(node1.left, node1.right)
        self._connectTwo(node2.left, node2.right)
        self._connectTwo(node1.right, node2.left) 

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self._connectTwo(root.left, root.right)
        return root
            
# @lc code=end

