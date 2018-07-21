class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        S = 0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                S -= roman[s[i]]
            else:
                S += roman[s[i]]
        S += roman[s[len(s)-1]]
        return S
            
            
