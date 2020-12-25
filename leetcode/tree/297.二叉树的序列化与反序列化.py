#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class TreeNode(object):
#     """
#     docstring
#     """
#     def __init__(self, x):
#         """
#         docstring
#         """
#         self.val = x
#         self.left = None
#         self.right = None


# preorder 
'''
class Codec:

    def _traverse_serialize(self, root):
        """
        docstring
        """
        temp = []
        if root == None:
            temp.append('#')
        else:
            temp.append(str(root.val))
            temp.extend(self._traverse_serialize(root.left))
            temp.extend(self._traverse_serialize(root.right))
        return temp

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return ','.join(self._traverse_serialize(root))
        
    def _traverse_deserialize(self, data_queue):
        """
        docstring
        """
        if data_queue.empty():
            return None
        # do not add while not empty() here
        data = data_queue.get()
        if data == '#':
            root = None
        else:
            root = TreeNode(data)
            root.left = self._traverse_deserialize(data_queue)
            root.right = self._traverse_deserialize(data_queue)
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        import queue
        data_queue = queue.Queue()
        data_list = data.split(',')
        for i in data_list:
            data_queue.put(i)
        return self._traverse_deserialize(data_queue)
'''

# postorder
'''
class Codec:

    def _traverse_serialize(self, root):
        """
        docstring
        """
        temp = []
        if root == None:
            temp.append('#')
        else:
            
            temp.extend(self._traverse_serialize(root.left))
            temp.extend(self._traverse_serialize(root.right))
            temp.append(str(root.val))
        return temp

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return ','.join(self._traverse_serialize(root))
        
    def _traverse_deserialize(self, data_list):
        """
        docstring
        """
        if data_list == []:
            return None
        # for postoder, root is on the rightest point, 
        # and we should tranverse to cover the tree from right to left
        # so we need to cover right sub tree first as well 
        data = data_list.pop()
        if data == '#':
            root = None
        else:
            root = TreeNode(data)
            root.right = self._traverse_deserialize(data_list)
            root.left = self._traverse_deserialize(data_list)
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(',')
        return self._traverse_deserialize(data_list)        
'''

# level order

class Codec:
            
    def serialize(self, root):
        import queue
        q = queue.Queue()

        data_list = []

        # we should return empty string but not None here
        if root == None:
            return ''

        q.put(root)
        while not q.empty():
            temp = q.get()

            if temp == None:
                data_list.append('#')
                continue
            data_list.append(str(temp.val))

            q.put(temp.left)
            q.put(temp.right)

        return ','.join(data_list)

    def deserialize(self, data):
        if data == '':
            return

        import queue
        q = queue.Queue()

        data_list = data.split(',')
        root = TreeNode(data_list[0])
        q.put(root)
        cursor = 0
        # we should record parents
        while not q.empty():
            parent = q.get()

            cursor += 1
            if data_list[cursor] != '#':
                parent.left = TreeNode(data_list[cursor])
                q.put(parent.left)
            
            cursor += 1
            if data_list[cursor] != '#':
                parent.right = TreeNode(data_list[cursor])
                q.put(parent.right)

        return root
                
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

