def lookup(root, x):
    if root == None:
        return False
    if root.val == x:
        return True
    if x < root.val:
        return lookup(root.left, x)
    else:
        return lookup(root.right, x)

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val > node.val:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build123a():
    root = TreeNode(2)
    left = TreeNode(1)
    right = TreeNode(3)

    root.left = left
    root.right = right

    return root

def build123b():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    return root

def build123c():
    root = TreeNode()
    insert(root, 2)
    root.insert(root, 1)
    root.insert(root, 3)

    return root

def size(node):
    """Given a binary tree, count the number of nodes in the tree."""
    if node == None:
        return 0
    return 1 + size(node.left) + size(node.right)

def max_depth(node):
    """Given a binary tree, compute its "maxDepth"; the
    number of nodes along the longest path from the root
    node down to the farthest leaf node.
    """

    if node == None:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))

def min_value(node):
    """Given a non-empty binary search tree (an ordered binary tree),
    return the minimum data value found in that tree."""

    while node.left is not None:
        node = node.left
    return node.val

def print_tree_inorder(node):
    """Given a binary search tree , iterate over the nodes
    to print them out in increasing order.
    """
    if not node:
        return
    print_tree_inorder(node.left)
    print(node.val)
    print_tree_inorder(node.right)

def print_tree_postorder(node):
    """Given a binary tree, print out the nodes of the tree
    according to a bottom-up "postorder" traversal -- both
    subtrees of a node are printed out completely before the
    node itself is printed, and each left subtree is printed
    before the right subtree. """

    if not node:
        return
    print_tree_postorder(node.left)
    print_tree_postorder(node.right)
    print(node.val)

def has_path_sum(node, target):
    """Given a binary tree and a sum, return true if the tree has a
    root-to-leaf path such that adding up all the values along the
    path equals the given sum. Return false if no such path can be found.
    """
    if not node:
        return target == 0
    return has_path_sum(node.left, target-node.val) or has_path_sum(node.right, target-node.val)

def print_paths(node):
    """Given a binary tree, print out all of its root-to-leaf paths."""
    path = []
    def print_paths_recur(node, path):
        if node is None:
            return
        path.append(node.val)
        if not node.left and not node.right:
            print(path)
        else:
            print_paths_recur(node.left, path[:])
            print_paths_recur(node.right, path[:])

    print_paths_recur(node, path)

def mirror(node):
    """Change a tree so that the roles of the left and right pointers
    are swapped at every node."""
    if not node.left or not node.right:
        return
    mirror(node.left)
    mirror(node.right)

    temp = node.left
    node.left = node.right
    node.right = temp

def double_tree(node):
    if node is None:
        return
    double_tree(node.left)
    double_tree(node.right)

    temp = TreeNode(node.val)
    temp.left = node.left
    node.left = temp

def same_tree(nodeA, nodeB):
    """Given two binary trees, return true if they are structurally identical."""
    # both empty
    if nodeA is None and nodeB is None:
        return True
    # both non-empty
    elif nodeA is not None and nodeB is not None:
        return ((nodeA.val == nodeB.val) and same_tree(nodeA.left, nodeB.left) and same_tree(nodeA.right, nodeB.right))
    # one empty
    else:
        print('one empty one not')
        return False

def count_trees(num):
    """Suppose you are building an N node binary search tree with the values 1..N. How many structurally different
    binary search trees are there that store those values?"""
    if num < 2:
        return 1
    count = 0
    for i in range(1,num+1):
        left = count_trees(i-1)
        right = count_trees(num-i)
        count += left*right
    return count

def is_bst(node):
    def is_bst_recur(node, int_min, int_max):
        if node is None:
            return True
        if node.val < int_min or node.val > int_max:
            return False
        return is_bst_recur(node.left, int_min, node.val)
        return is_bst_recur(node.right, node.val+1, int_max)
    return is_bst_recur(node, int_min, int_max)
