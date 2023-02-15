class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []

        for i, c in enumerate(num):
            while k and s and int(c) < int(s[-1]):
                s.pop()
                k -= 1
            s.append(c)

        while s and k:
            s.pop()
            k -= 1

        res = ''.join(s)
        for i in range(len(res)):
            if res[i] != '0':
                break
        res = res[i:]
        return res if res else "0"
