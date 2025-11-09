# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Hold maximum diameter
        self.res = 0

        # Recursive function
        def dfs(curr):

            # Base case
            if not curr:
                return 0

            # Recursive calls
            left = dfs(curr.left)
            right = dfs(curr.right)            

            self.res = max(self.res, left + right) # Update global longest path 
            return 1 + max(left, right) # Return height of curr subtree

        dfs(root)
        return self.res # Return max num of edges