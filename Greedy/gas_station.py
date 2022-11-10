from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [g - c for g, c in zip(gas, cost)]
        if sum(diff) < 0:
            return -1

        doubled = diff + diff  # double the array because we have to do a circuit
        best_start = self.maxSubArrayStart(doubled) % len(diff)  # convert back to original index

        credit = 0
        index = best_start
        for i in range(len(diff) + 1):
            credit += doubled[index]
            if credit < 0:
                return -1
            index += 1

        return best_start

    def maxSubArrayStart(self, vals):
        res = -math.inf
        cur_max = -math.inf
        l, index = 0, 0

        for i in range(len(vals)):
            if vals[i] > cur_max + vals[i]:
                l = i

            cur_max = max(cur_max + vals[i], vals[i])

            if cur_max > res:
                res = cur_max
                index = l
        return index