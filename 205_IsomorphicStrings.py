class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        if len(s) != len(t):
            return false
        else:
            for i in range(0, len(s)):
                #Kiểm tra s[i] đã có hay chưa
                if s[i] not in dic:
                    #Kiểm tra t[i] đã tồn tại hay chưa
                    if t[i] in dic.values():
                        return False
                    #Thêm vào từ điển
                    dic[s[i]] = t[i]
                else:
                    #Kiểm tra giá trị
                    if dic[s[i]] != t[i]:
                        return False   
            return True
