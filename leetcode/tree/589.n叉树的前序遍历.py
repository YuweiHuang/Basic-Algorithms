#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# class Node(object):
#     """
#     docstring
#     """
#     def __init__(self, val = None, children = None):
#         """
#         docstring
#         """
#         self.val = val
#         self.children = children

# recurse
# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         children_list = []
#         if root == None:
#             return

#         children_list.append(root.val)
#         for child in root.children:
#             children_list.extend(self.preorder(child))
#         return children_list

# iterate
# 1. put children from right to left into the stack, so that children on the left can be iterate first
class Solution(object):
    
    def preorder(self, root):
        """
        docstring
        """
        children_list = []
        s = []
        s.append(root)
        while s != []:
            temp = s.pop(-1)
            if temp == None:
                continue
            children_list.append(temp.val)
            for child in temp.children[::-1]:
                s.append(child)
        return children_list
        
# @lc code=end

