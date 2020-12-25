#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
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
    def __init__(self, val, left=None, right=None):
        """
        docstring
        """
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # inOrder traverse, DFS
    # DFS 是不断找下去直到节点为空，这样能够找到最深的地方； BFS是优先遍历所有子树，如果达到某一条件就停止，那么是找最近。
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# @lc code=end

