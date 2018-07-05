class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        st1 = "";
        st2 = "";
        for i in S:
            if i == "#":
                st1 = st1[:len(st1)-1:]
            else:
                st1 = st1 + i
        for i in T:
            if i == "#":
                st2 = st2[:len(st2)-1:]
            else:
                st2 = st2 + i
        return st1 == st2