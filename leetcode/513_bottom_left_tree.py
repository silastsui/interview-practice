# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #bfs tree traversal

        queue = [root]
        while len(queue) > 0:
            node = queue[0]
            queue.pop(0)
            if node.right is not None:
                queue.append([node.right])
            if node.left is not None:
                queue.append([node.left])

        return node.val
