class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1


        sorted_keys = sorted(seen, key=lambda x: seen[x], reverse=True)

        return sorted_keys[:k]