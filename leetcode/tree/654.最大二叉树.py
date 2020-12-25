#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) < 1:
            return None
        max_val = nums[0]
        max_index = 0
        for i in range(len(nums)):
            if nums[i] > max_val:
                max_index = i
                max_val = nums[i]
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(nums[0:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index+1:len(nums)])
        return root
        
# @lc code=end

