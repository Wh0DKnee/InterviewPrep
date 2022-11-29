class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        left = 1 << 31
        right = 1

        for i in range(32):
            is_one = (left & n) != 0
            if is_one:
                res = right | res
            left = left >> 1
            right = right << 1

        return res
