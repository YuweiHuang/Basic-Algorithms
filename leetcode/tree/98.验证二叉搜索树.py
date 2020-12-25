#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __traverse(self, root, min_node, max_node):
        """
        docstring
        """
        if root == None:
            return True

        if min_node != None and root.val <= min_node.val:
            return False

        if max_node != None and root.val >= max_node.val:
            return False

        return self.__traverse(root.left, min_node, root) and self.__traverse(root.right, root, max_node)
        

    def isValidBST(self, root: TreeNode) -> bool:
        return self.__traverse(root, None, None)
        

# @lc code=end

