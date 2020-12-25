#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class TreeNode(object):
#     """
#     docstring
#     """
#     def __init__(self, x):
#         """
#         docstring
#         """
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def minDepth(self, root: TreeNode) -> int:
        # count to leaf!!!! but not other nodes
        if root == None:
            return 0

        if root.left == None and root.right != None:
            return 1 + self.minDepth(root.right)
        if root.right == None and root.left != None:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        
        

# @lc code=end

