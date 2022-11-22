from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for pre in prerequisites:
            adj[pre[0]].append(pre[1])

        visited = set()
        done = set()

        def dfs(k):
            visited.add(k)
            loop = False
            for nei in adj[k]:
                if nei in visited and nei not in done:
                    return True
                if nei not in visited:
                    loop = loop or dfs(nei)
            done.add(k)
            return loop

        for key in adj:
            if key not in visited:
                if dfs(key):
                    return False

        return True
