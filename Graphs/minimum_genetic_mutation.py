from typing import List
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene != startGene and endGene not in bank:
            return -1

        def bfs(start):
            q = deque([(start, 0)])
            visited = {start}
            while q:
                cur, count = q.pop()
                if cur == endGene:
                    return count
                for gene in bank:
                    if gene not in visited and self.isMutation(cur, gene):
                        visited.add(gene)
                        q.appendleft((gene, count + 1))

            return -1

        return bfs(startGene)

    def isMutation(self, a, b):
        diff = 0
        for c1, c2 in zip(a, b):
            if c1 != c2:
                diff += 1
        return diff == 1
