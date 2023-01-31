from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        # idea: repeated dfs on graph, whenever we find a cycle, shrink it into a single node.
        # observation: with at most one outgoing edge per node, each connected component can
        # have at most one cycle. (Where does the intuition for this come from? Draw two cycles.
        # Since all nodes in the cycle already have one outgoing edge, these nodes cannot point
        # to any other nodes. Other nodes might point into one of the cycles, but cannot point
        # to both cycles)
        # new idea: collapsing is not needed due to the observation

        dist = {}  # edge distance for each node from start node of the search
        done = set()  # keep track of nodes that are finished so we don't do duplicate work

        def find_cycle(node, parent, cur_dist):
            res = -1
            if node in done:
                return res
            if node in dist:
                return dist[parent] - dist[node] + 1

            dist[node] = cur_dist
            if edges[node] != -1:
                res = find_cycle(edges[node], node, cur_dist + 1)

            done.add(node)
            return res

        res = -1
        for i in range(len(edges)):
            if i not in dist:
                res = max(res, find_cycle(i, None, 0))

        return res
