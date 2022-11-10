from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        straights = [[] for i in range((len(hand) // groupSize))]

        for num in hand:
            appended = False
            for straight in straights:
                if len(straight) == groupSize:
                    continue
                if not straight:
                    straight.append(num)
                    appended = True
                    break
                if straight[-1] == num - 1:
                    straight.append(num)
                    appended = True
                    break
            if not appended:
                return False

        return True