#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        """
        docstring
        """
        self.sum_val = 0

    def traverse(self, root):
        """
        docstring
        """
        if root == None:
            return
        else:
            self.traverse(root.right)
            # only add value of each node but not add value of sum
            # record value before change root value
            self.sum_val += root.val
            root.val = self.sum_val
            self.traverse(root.left)

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        return root
        
# @lc code=end

