class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            added = 0
            while n:
                digit = n % 10
                added += digit**2
                n = n // 10
            if added == 1:
                return True
            if added in seen:
                return False
            if n == 0:
                n = added
            seen.add(added)

    # more elegant solution without using additional memory
    # uses Floyd's tortoise and hare algorithm for cycle detection,
    # see Linked_List/linked_list_cycle.py
    def isHappy_elegant(self, n: int) -> bool:
        slow, fast = n, self.sumSquareDigits(n)

        while slow != fast:
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)

        return True if fast == 1 else False

    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output
