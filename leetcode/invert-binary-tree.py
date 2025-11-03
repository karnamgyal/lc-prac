# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
         # Base case - end when reach an empty node
        if not root:
            return None

        # Swap left and right children of root
        root.left, root.right = root.right, root.left

        # Recursively invert down left path and right path
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root;