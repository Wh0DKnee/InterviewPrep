from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strs:
            char_count = [0] * 26
            for c in s:
                char_count[ord(c) % 26] += 1
            dic[tuple(char_count)].append(s)

        return list(dic.values())
