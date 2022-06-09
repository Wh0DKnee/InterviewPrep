class Solution:
    def hammingWeight(self, n: int) -> int:
        index = 1 << 31
        weight = 0
        while index:
            weight += 1 if index & n else 0
            index = index >> 1

        return weight
