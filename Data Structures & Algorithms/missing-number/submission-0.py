class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = sorted(set(nums))
        l = len(seen)
        j = 0

        for i in range(l):
            if seen[i] == j:
                j += 1
            else:
                return j

        return j