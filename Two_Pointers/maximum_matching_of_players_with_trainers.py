from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        p, t, res = 0, 0, 0
        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                res += 1
                p += 1
                t += 1
            else:
                p += 1
        return res
