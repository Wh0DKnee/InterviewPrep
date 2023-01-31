from typing import List
import math
from collections import deque


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        def bfs(node, dist_dict):
            visited = set()
            visited.add(node)
            visited.add(-1)
            q = deque()
            q.append(node)
            dist = 0
            while q:
                cur = q.pop()
                dist_dict[cur] = dist
                if edges[cur] not in visited:
                    visited.add(edges[cur])
                    q.appendleft(edges[cur])
                dist += 1

        res = [(math.inf, math.inf)]
        visited = set()

        def dfs(node):
            visited.add(node)
            if node in node1_dict and node in node2_dict:
                dist = max(node1_dict[node], node2_dict[node])
                if dist < res[0][0] or dist == res[0][0] and node < res[0][1]:
                    res[0] = (dist, node)

            if edges[node] not in visited:
                dfs(edges[node])

        node1_dict, node2_dict = {}, {}
        bfs(node1, node1_dict)
        bfs(node2, node2_dict)
        dfs(node1)

        return res[0][1] if res[0][0] != math.inf else -1
