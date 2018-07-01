# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return

        def d(root):
            if root is None:
                return

            root.left, root.right = root.right, root.left

            d(root.left)
            d(root.right)

        d(root)
        return root
