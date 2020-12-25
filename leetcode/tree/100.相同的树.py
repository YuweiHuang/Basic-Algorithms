#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode(object):
    """
    docstring
    """
    def __init__(self, val=0, left=None, right=None):
        """
        docstring
        """
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        else:
            if p == None or q == None:
                return False
            else:
                return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
# @lc code=end

