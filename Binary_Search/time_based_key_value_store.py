from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # edge cases
        if key not in self.dict or self.dict[key][0][1] > timestamp:
            return ""
        vals = self.dict[key]
        if vals[-1][1] < timestamp:
            return vals[-1][0]

        # binary search
        l, r = 0, len(vals) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if vals[m][1] == timestamp:
                return vals[m][0]
            if vals[m][1] < timestamp:
                l = m + 1
            else:
                r = m - 1
        return vals[m - 1][0]