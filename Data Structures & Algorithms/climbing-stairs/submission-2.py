class Solution:
    def climbStairs(self, n: int) -> int:
        small, big = 1, 2
        for _ in range(n - 2):
            small, big = big, small + big
        return big if n > 1 else 1