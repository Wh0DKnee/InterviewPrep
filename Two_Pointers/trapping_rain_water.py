from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = [0], [0]
        water = 0

        for i in range(1, len(height)):
            left.append(max(left[-1], height[i - 1]))

        for i in range(len(height) - 2, -1, -1):
            right.append(max(right[-1], height[i + 1]))

        right.reverse()

        for i in range(len(height)):
            if height[i] < left[i] and height[i] < right[i]:
                water += min(left[i] - height[i], right[i] - height[i])

        return water
