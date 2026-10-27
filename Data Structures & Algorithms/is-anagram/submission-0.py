class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        seem = {}
        for val in s:
            if val in seen :
                seen[val] += 1
            else:
                seen[val] = 1    
        for val1 in t:
            if val1 in seem :
                seem[val1] += 1
            else:
                seem[val1] = 1 

        if  seen == seem :         
            return True
        else:
            return False    