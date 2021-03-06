#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # bad cases
        if root == None:
            return None
        if root == p or root == q:
            return root

        # traverse
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # case 1: p and q both in root based tree
        if left != None and right != None:
            return root

        # case 2: p and q not in root based tree
        if left == None and right == None:
            return None

        # case 3: p in or q in root based tree
        if left:
            return left
        if right:
            return right


        
        
# @lc code=end

