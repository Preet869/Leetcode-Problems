class Solution(object):
    def isAnagram(self, s, t):
        if len(t) != len(s):
            return False
        count = {}
        for i in s:
            if i in count:
                count[i] = count[i] + 1
            else: 
                count[i] = 1
        for i in t:
            if i not in count:
                return False
            else:
                count[i] -= 1
        for i in count:
            if count[i] != 0:
                return False
        return True
        
