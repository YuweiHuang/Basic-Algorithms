#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
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
    def __init__(self, x = 0, left = None, right = None):
        """
        docstring
        """
        self.val = x
        self.left = left
        self.right = right

class Solution:

    def __traverse(self, root, data_list):
        """
        docstring
        """
        if root == None:
            return

        self.__traverse(root.left, data_list)
        self.__traverse(root.right, data_list)
        data_list.append(root.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        data_list = []
        self.__traverse(root, data_list)
        return data_list
# @lc code=end

