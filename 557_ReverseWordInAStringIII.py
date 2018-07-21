class Solution: 
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        L = []
        st = ""
        for letter in s:
            if letter != ' ':
                st += letter
            else:
                L.append(st[::-1])
                st = ""
        L.append(st[::-1])
        result = ""
        for string in L:
            result += ' ' + string
        return result[1::]
