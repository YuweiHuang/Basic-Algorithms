#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) < 1:
            return None
        root_val = postorder[-1]
        root_index = 0
        for i in range(len(inorder)):
            if inorder[i] == root_val:
                root_index = i
                break
            
        left_size = root_index

        root = TreeNode(root_val)
        root.left = self.buildTree(inorder[0 : root_index], postorder[0 : left_size])
        root.right = self.buildTree(inorder[root_index+1 : len(inorder)], postorder[left_size : -1])
        return root
# @lc code=end

