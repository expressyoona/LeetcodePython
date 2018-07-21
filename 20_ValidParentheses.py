class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parent = {'{':'}','[':']','(':')'}
        stack = []
        for letter in s:
            if letter in parent:
                stack.append(letter)
            else:
                if len(stack) <= 0:
                    return False
                close = stack.pop()
                if letter != parent[close]:
                    return False
        return len(stack) == 0
