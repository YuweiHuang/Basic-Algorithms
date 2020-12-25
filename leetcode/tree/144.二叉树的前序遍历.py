#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __traverse(self, root, data_list):
        """
        docstring
        """
        if root == None:
            return
        data_list.append(root.val)
        self.__traverse(root.left, data_list)
        self.__traverse(root.right, data_list)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        data_list = []
        self.__traverse(root, data_list)
        return data_list
        
# @lc code=end

