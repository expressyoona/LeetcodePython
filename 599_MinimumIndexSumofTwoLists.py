class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        result = []
        Max = float('inf')
        for index in range(len(list1)):
            if list1[index] in list2:
                S = index + list2.index(list1[index])
                if S < Max:
                    #print(S, '<', Max)
                    result = []
                    result.append(list1[index])
                    Max = S
                elif S == Max:
                    result.append(list1[index])
                else:
                    pass
        return result
