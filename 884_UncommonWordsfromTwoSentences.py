class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
        def count(sentence):
            words = sentence.split(' ')
            dic = {}
            for word in words:
                if word not in dic:
                    dic[word] = 1
                else:
                    dic[word] += 1
            return dic
        
        result = []
        
        dicA = count(A)
        dicB = count(B)
        
        def find(first, second):
            res = []
            for word in first:
                if first[word] == 1 and word not in second:
                    res.append(word)
            return res
                
        return find(dicA, dicB) + find(dicB, dicA)
        
        
        
        
