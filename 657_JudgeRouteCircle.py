class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        h = 0
        v = 0
        for i in moves:
            if i == "U":
                h += 1
            if i == "D":
                h -= 1
            if i == "L":
                v -= 1
            if i == "R":
                v += 1
        return h == 0 and v == 0
        
