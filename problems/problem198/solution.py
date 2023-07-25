from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        elif n == 1:
            return nums[0]

        # Create an array dp to store the maximum money that can be robbed up to the current house.
        dp = [0] * n

        # Base cases: The maximum money that can be robbed for the first two houses.
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # Calculate the maximum money that can be robbed up to the current house by considering
            # whether to rob the current house or not (avoid robbing adjacent houses).
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # Return the maximum money that can be robbed at the last house.
        return dp[n - 1]

# Input: nums = [2, 7, 9, 3, 1]
def main():
    nums = [2, 7, 9, 3, 1]
    solution = Solution()
    result = solution.rob(nums)
    print(result)
