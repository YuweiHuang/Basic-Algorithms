#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __traverse_left(self, root, data_list):
        """
        docstring
        """
        if root == None:
            data_list.append('#')
            return
        data_list.append(root.val)
        self.__traverse_left(root.left, data_list)
        self.__traverse_left(root.right, data_list)

    def __traverse_right(self, root, data_list):
        """
        docstring
        """
        if root == None:
            data_list.append('#')
            return
        data_list.append(root.val)
        self.__traverse_right(root.right, data_list)
        self.__traverse_right(root.left, data_list)

    def isSymmetric(self, root: TreeNode) -> bool:
        left_traverse = []
        right_traverse = []
        if root == None:
            return True
        self.__traverse_left(root.left, left_traverse)
        self.__traverse_right(root.right, right_traverse)
        if left_traverse == right_traverse:
            return True
        else:
            return False
# @lc code=end

