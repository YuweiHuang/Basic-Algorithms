#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        """
        docstring
        """
        self.sum_val = 0

    def traverse(self, root):
        """
        docstring
        """
        if root == None:
            return
        else:
            self.traverse(root.right)
            self.sum_val += root.val
            root.val = self.sum_val
            self.traverse(root.left)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        return root
        
# @lc code=end

