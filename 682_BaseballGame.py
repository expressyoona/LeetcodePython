class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        point, S, L = 0, 0, [0]
        for letter in ops:
            if letter == "C":
                S = S - L.pop()
                point = L[len(L) - 1]
            elif letter == "D":
                point = point * 2
                S = S + point
                L.append(point)
            elif letter == "+":
                point = L[len(L) - 1] + L[len(L) - 2]
                S = S + point
                L.append(point)
            else:
                point = int(letter)
                S = S + point
                L.append(point)
        return S
