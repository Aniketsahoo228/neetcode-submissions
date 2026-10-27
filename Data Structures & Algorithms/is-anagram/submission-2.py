class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        seem = {}
        seen = {}

        for val in s:
            seem[val] = seem.get(val , 0 ) + 1
        for val1 in t:
            seen[val1] = seen.get(val1 , 0) + 1

        if seen == seem:
            return True
        else:
            return False            
