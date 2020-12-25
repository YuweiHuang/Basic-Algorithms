#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
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
    def __init__(self, x, left, right):
        """
        docstring
        """
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        # copy sub trees
        left = root.left
        right = root.right
        
        # move left subtree to right
        root.left = None
        root.right = left

        # we should not connect bind left to the end of right dirrectly, but go across it first
        p = root
        while p.right:
            p = p.right
        p.right = right



# @lc code=end

