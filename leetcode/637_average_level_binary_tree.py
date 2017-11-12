# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        #basic bfs
        queue = [root]
        avg_values = []
        while len(queue) > 0:
            avg_values.append(sum([node.val for node in queue])*1.0/len(queue))

            for node in queue[:]:
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                queue.pop(0)
        return avg_values
