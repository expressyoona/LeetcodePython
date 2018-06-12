# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        a = self.maxDepth(root.left)
        b = self.maxDepth(root.right)
        if a > b:
            return a + 1
        else:
            return b + 1
        
        