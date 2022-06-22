

class Solution:
    # O(n^2)
    def can_attend_meetings_brute_force(self, intervals):
        for i in range(len(intervals) - 1):
            for j in range(i+1, len(intervals)):
                if intervals[i][0] < intervals[j][0] < intervals[i][1]:
                    return False
        return True

    # O(n logn)
    def can_attend_meetings_sort(self, intervals):
        intervals.sort(key = lambda i: i[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True


intervals = [(5,8),(9,15)]
sol = Solution()
print(sol.can_attend_meetings_sort(intervals))
