#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode(object):
    """
    docstring
    """
    def __init__(self, x):
        """
        docstring
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            temp = TreeNode(root.val)
            temp.left = self.invertTree(root.right)
            temp.right = self.invertTree(root.left)
            return temp
        else:
            return None

# @lc code=end

