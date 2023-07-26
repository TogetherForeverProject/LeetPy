from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Check if the nums list is empty, return 0 if it is.
        if not nums:
            return 0

        # Create an array 'house' to store the sum of values based on their count and index.
        # The index represents the value, and the value at that index represents the sum of that value in the nums list.
        house = [0] * (max(nums) + 1)
        for num in nums:
            house[num] += num

        # Initialize 'prev' and 'curr' variables to keep track of the maximum points while iterating through the 'house' array.
        prev = curr = 0

        # Iterate through the 'house' array and calculate the maximum points using dynamic programming approach.
        for i in range(1, len(house)):
            prev, curr = curr, max(house[i] + prev, curr)

        # Return the maximum points earned.
        return curr


# Input: nums = [3, 4, 2]
def main():
    nums = [3, 4, 2]
    solution = Solution()
    max_points = solution.deleteAndEarn(nums)
    print(max_points)
