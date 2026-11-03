class Solution:
    def isPalindrome(self, s: str) -> bool:
        val = ""
        for ch in s:
            if ch.isalnum():
                val += ch.lower()
        return val == val[::-1]
                               

