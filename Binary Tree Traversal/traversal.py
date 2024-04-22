"""
Binary Tree Traversal.
"""

class Node:
    """
    Node.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order(root):
    """
    Pre.
    """
    if root is None:
        return []
    result = [root.data]
    result += pre_order(root.left)
    result += pre_order(root.right)
    return result

def in_order(root):
    """
    In.
    """
    if root is None:
        return []
    result = in_order(root.left)
    result.append(root.data)
    result += in_order(root.right)
    return result

def post_order(root):
    """
    Post.
    """
    if root is None:
        return []
    result = post_order(root.left)
    result += post_order(root.right)
    result.append(root.data)
    return result
