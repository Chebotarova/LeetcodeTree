"""
Delete Node in a BST.
"""

class TreeNode:
    """
    TreeNode.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Solution.
    """
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Delete node.
        """
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            successor = self.findSuccessor(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        return root

    def findSuccessor(self, node: TreeNode) -> TreeNode:
        """
        Find successor.
        """
        while node.left:
            node = node.left
        return node
