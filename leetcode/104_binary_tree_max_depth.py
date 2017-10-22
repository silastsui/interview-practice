# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max = 0
        count = 0
        def preorder(node, max, count):
            if node is not None:
                count += 1
                preorder(node.left)
                count -= 1
                prorder(node.right)
            if count > max:
                max = count
            return max

        return preorder(root, max, count)
