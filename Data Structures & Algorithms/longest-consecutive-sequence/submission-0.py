class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = sorted(set(nums))   
        longest = 1                
        current = 1                
        i = 0

        while i < len(seen) - 1:
            if seen[i + 1] - seen[i] == 1:
                current += 1       
            else:
                current = 1      
            longest = max(longest, current)
            i += 1

        return longest