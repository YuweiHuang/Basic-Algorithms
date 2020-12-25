#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) < 1:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_index = 0
        for i in range(len(inorder)):
            if root_val == inorder[i]:
                root_index = i
                break
        left_size = root_index

        root.left = self.buildTree(preorder[1 : 1 + left_size], inorder[0 : root_index])
        root.right = self.buildTree(preorder[left_size + 1 : len(preorder)], inorder[root_index + 1 : len(inorder)])
        return root

        
        
        

        

# @lc code=end

