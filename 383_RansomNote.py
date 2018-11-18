class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        def getLetter(sentence):
            res = {}
            for letter in sentence:
                if letter not in res:
                    res[letter] = 1
                else:
                    res[letter] += 1
            return res
        
        ransom = getLetter(ransomNote)
        maga = getLetter(magazine)
        for letter, quantity in ransom.items():
            if letter not in maga:
                return False
            elif quantity > maga[letter]:
                return False
        return True
