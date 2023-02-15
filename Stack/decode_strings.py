class Solution:
    def decodeString(self, expr: str) -> str:
        s = []

        for c in expr:
            if c == "]":
                word = deque()
                while s[-1] != "[":
                    word.appendleft(s.pop())
                word = ''.join(word)
                s.pop()  # remove "["

                times = 0
                exponent = 0
                while s and s[-1].isdigit():
                    digit = int(s.pop())
                    times += digit * (10 ** exponent)
                    exponent += 1

                repeated = []
                for _ in range(times):
                    repeated.append(word)
                repeated = ''.join(repeated)
                s.append(repeated)
            else:
                s.append(c)

        return ''.join(s)