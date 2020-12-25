#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse(self, root, data_list):
        """
        docstring
        """
        if root == None:
            return
        else:
            self.traverse(root.left, data_list)
            data_list.append(root.val)
            self.traverse(root.right, data_list)


    def kthSmallest(self, root: TreeNode, k: int) -> int:
        data_list = []
        self.traverse(root, data_list)
        return data_list[k-1]
        
        
# @lc code=end

