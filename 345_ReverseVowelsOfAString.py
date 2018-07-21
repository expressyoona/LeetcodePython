class Solution:
    def isVowels(self, t):
        return t == 'u' or t == 'e' or t == 'o' or t == 'a' or t == 'i' or t == 'U' or t == 'E' or t == 'O' or t == 'A' or t == 'I'
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = []
        rs = ""
        for i in s:
            if self.isVowels(i):
                vowels.append(i)
        for i in s:
            if not self.isVowels(i):
                rs = rs + i
            else:
                rs = rs + vowels.pop()
        return rs
                
        
        
