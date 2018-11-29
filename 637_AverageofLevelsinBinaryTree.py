# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            s = sum(x.val for x in queue)
            result.append(s / len(queue))
            queue = [child for current in queue for child in (current.left, current.right) if child]
            
        return result
