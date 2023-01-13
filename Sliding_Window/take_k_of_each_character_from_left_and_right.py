class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counts = {c: s.count(c) for c in ["a", "b", "c"]}
        if not all(val >= k for _, val in counts.items()):
            return -1

        l = 0
        max_window = 0

        for r in range(len(s)):
            counts[s[r]] -= 1
            while not all(val >= k for _, val in counts.items()):
                counts[s[l]] += 1
                l += 1
            max_window = max(max_window, r - l + 1)

        return len(s) - max_window
