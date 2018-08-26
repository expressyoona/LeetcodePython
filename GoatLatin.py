class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        def isVowel(letter):
            return letter in {'u', 'e', 'o', 'a', 'i', 'U', 'E', 'O', 'A', 'I'}
        words = S.split(' ')
        index = 1
        L = []
        w = ''
        for word in words:
            if isVowel(word[0]):
                w = word + 'ma'
            else:
                w = word[1::] + word[0] + 'ma'
            w += 'a' * index
            L.append(w)
            index += 1
        return ' '.join(L)
        
