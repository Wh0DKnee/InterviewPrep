class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        new_dp = [0, 0, 0]
        dp[nums[-1]%3] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            rem = nums[i] % 3
            if rem == 0:
                new_dp[0] = dp[0] + nums[i]
                new_dp[1] = 0 if dp[1] == 0 else dp[1] + nums[i]
                new_dp[2] = 0 if dp[2] == 0 else dp[2] + nums[i]
            elif rem == 1:
                new_dp[0] = max(dp[2] + nums[i], dp[0])
                new_dp[1] = max(dp[0] + nums[i], dp[1])
                new_dp[2] = max(dp[1] + nums[i], dp[2])
            else: # rem == 2
                new_dp[0] = max(dp[1] + nums[i], dp[0])
                new_dp[1] = max(dp[2] + nums[i], dp[1])
                new_dp[2] = max(dp[0] + nums[i], dp[2])
            dp, new_dp = new_dp, dp

        return dp[0]