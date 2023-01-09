class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res, cur = 0, 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(k):
            if s[i] in vowels:
                cur += 1
        res = cur

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                cur -= 1
            if s[i] in vowels:
                cur += 1
            res = max(res, cur)

        return res
