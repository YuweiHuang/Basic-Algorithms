#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # inOrder traverse
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            t3 = TreeNode(t1.val + t2.val)
            t3.left = self.mergeTrees(t1.left, t2.left)
            t3.right = self.mergeTrees(t1.right, t2.right)

        elif t1 == None and t2 != None:
            t3 = TreeNode(t2.val)
            t3.left = self.mergeTrees(None, t2.left)
            t3.right = self.mergeTrees(None, t2.right)

        elif t1 != None and t2 == None:
            t3 = TreeNode(t1.val)
            t3.left = self.mergeTrees(t1.left, None)
            t3.right = self.mergeTrees(t1.right, None)

        else:
            t3 = None
        return t3
        
# @lc code=end

