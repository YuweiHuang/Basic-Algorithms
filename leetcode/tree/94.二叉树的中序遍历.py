#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution:
    def __traverse(self, root, data_list):
        """
        docstring
        """
        if root == None:
            return
        self.__traverse(root.left, data_list)
        data_list.append(root.val)
        self.__traverse(root.right, data_list)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        data_list = []
        self.__traverse(root, data_list)
        return data_list
        
        
# @lc code=end

