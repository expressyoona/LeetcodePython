# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    tilt = 0
    def traverse(self, root):
        if not root:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.tilt += abs(left - right)
        return left + right + root.val
        
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root)
        return self.tilt
