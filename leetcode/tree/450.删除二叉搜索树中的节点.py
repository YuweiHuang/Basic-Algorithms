#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __getMin(self, node):
        """
        find the minimum node to replace
        """
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return None

        # reach the node
        if root.val == key:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            # both left and right not null
            else:
                # search the most left node in its right sub tree
                min_node = self.__getMin(root.right)
                # replace the value of the node and repointer the right sub tree
                root.val = min_node.val
                # replace and delete recursively
                root.right = self.deleteNode(root.right, min_node.val)
                return root

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root
            
        
# @lc code=end

