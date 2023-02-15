from collections import deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque()
        visited = set()
        q.append(0)
        prev_max = -1

        while q:
            cur = q.pop()
            if cur == len(s) - 1:
                return True
            for i in range(max(cur + minJump, prev_max + 1), cur + maxJump + 1):
                if i < len(s) and s[i] == '0':
                    q.appendleft(i)
            prev_max = cur + maxJump

        return False
