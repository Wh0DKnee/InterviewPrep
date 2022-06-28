from typing import List
import math


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        res = [0 for i in range(n + 1)]
        res[1] = 1
        for i in range(2, n + 1):
            res[i] = 1 + res[i % (2 ** (int(math.log(i, 2))))]
        return res
