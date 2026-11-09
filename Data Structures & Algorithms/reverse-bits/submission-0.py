class Solution:
    def reverseBits(self, n: int) -> int:
        num = bin(n)[2:].zfill(32)
        i = len(num) - 1
        val = ""

        while i >= 0:
            val = val + str(num[i])
            i -= 1

        return int(val, 2)