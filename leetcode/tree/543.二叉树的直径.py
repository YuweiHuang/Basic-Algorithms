#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        """
        docstring
        """
        self._max_len = 0

    def __traverse(self, root):
        """
        docstring
        """
        if root == None:
            return 0
        else:
            left = self.__traverse(root.left)
            right = self.__traverse(root.right)
            # update global state
            self._max_len = max(left + right, self._max_len)
            return max(left, right) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        _ = self.__traverse(root)
        return self._max_len
        
# @lc code=end

