class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = "qwertyuiop"
        row2 = "asdfghjklASDFGHJKL"
        row3 = "zxcvbnmZXCVBNM"
        L = []
        def sameRow(word):
            check1 = False
            check2 = False
            check3 = False
            for letter in word:
                if letter in row1:
                    if not check2 and not check3:
                        check1 = True
                    else:
                        return False
                if letter in row2:
                    if not check1 and not check3:
                        check2 = True
                    else:
                        return False
                if letter in row3:
                    if not check1 and not check2:
                        check3 = True
                    else:
                        return False
            return True
        for word in words:
            if sameRow(word):
                L.append(word)
        return L