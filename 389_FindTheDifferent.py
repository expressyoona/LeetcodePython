class Solution:
    def findTheDifference(self, s, t):
        s1, s2 = 0, 0
        for letter in s:
            s1 += ord(letter)
        for letter in t:
            s2 += ord(letter)
        return chr(abs(s1-s2))
