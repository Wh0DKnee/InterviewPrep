from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lookup = {}

        for i, c in enumerate(s):
            if c not in lookup:
                lookup[c] = len(res)
                res.append(1)
            else:
                summed = sum(res[lookup[c]:])
                res = res[0:lookup[c]]
                res.append(summed + 1)

                start = False
                for k in lookup:
                    if k == c:
                        start = True
                    if start:
                        lookup[k] = lookup[c]

        return res
