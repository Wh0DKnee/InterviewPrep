from collections import deque, defaultdict
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(lambda: {"r": [], "b": []})
        for start, end in redEdges:
            adj_list[start]["r"].append(end)

        for start, end in blueEdges:
            adj_list[start]["b"].append(end)

        res = [-1] * n

        visited_from_red = {0}
        visited_from_blue = {0}
        q = deque()
        q.append((0, "r"))
        q.append((0, "b"))
        dist = 0
        while q:
            for _ in range(len(q)):
                cur, color = q.pop()
                if res[cur] == -1:   # might visit a node twice, so need this check.
                    res[cur] = dist  # the first time always has the smaller dist
                if color == "r":
                    for nei in adj_list[cur]["b"]:
                        if nei not in visited_from_blue:
                            visited_from_blue.add(nei)
                            q.appendleft((nei, "b"))
                else:
                    for nei in adj_list[cur]["r"]:
                        if nei not in visited_from_red:
                            visited_from_red.add(nei)
                            q.appendleft((nei, "r"))
            dist += 1
        return res
