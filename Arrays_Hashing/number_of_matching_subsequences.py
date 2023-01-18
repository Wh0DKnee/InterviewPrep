from typing import List
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        res = 0

        for w in words:
            waiting[w[0]].append(w[1:])

        for c in s:
            for rest in waiting.pop(c, []):
                if len(rest) == 0:
                    res += 1
                else:
                    waiting[rest[0]].append(rest[1:])

        return res

    # This was close to the actual solution, but I didn't think of creating
    # a data structure to efficiently find the words that are currently waiting
    # for a certain character.
    def secondTrieTLE(self, s, words):
        indices = [0] * len(words)
        for c in s:
            for i in range(len(indices)):
                if indices[i] < len(words[i]) and c == words[i][indices[i]]:
                    indices[i] += 1

        return sum([indices[i] >= len(words[i]) for i in range(len(words))])

    def bruteForceTLE(self, s, words):
        res = 0
        for word in words:
            idx = 0
            for c in s:
                if c == word[idx]:
                    idx += 1
                if idx >= len(word):
                    res += 1
                    break

        return res