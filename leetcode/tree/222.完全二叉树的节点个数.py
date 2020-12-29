#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
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
    def countNodes(self, root: TreeNode) -> int:
        left = root
        right = root
        heigh_left = 0
        heigh_right = 0
        while left:
            left = left.left
            heigh_left += 1

        while right:
            right = right.right
            heigh_right += 1

        # complete sub tree
        if heigh_left == heigh_right:
            return 2 ** heigh_left - 1

        # a not complete sub tree
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# @lc code=end

