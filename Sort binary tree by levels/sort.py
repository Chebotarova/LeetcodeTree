"""
Sort binary tree by levels.
"""

from collections import deque

class Node:
    """
    Node.
    """
    def __init__(self, L=None, R=None, n=None):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(root):
    """
    Tree by levels.
    """
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
