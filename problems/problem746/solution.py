from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        # Initialize variables to keep track of the minimum cost to reach the previous two steps.
        prev1 = cost[0]
        prev2 = cost[1]

        for i in range(2, n):
            # Calculate the minimum cost to reach the current step by choosing the
            # minimum cost between the previous two steps.
            current = cost[i] + min(prev1, prev2)
            prev1, prev2 = prev2, current

        # Finally, return the minimum cost to reach the top floor, which is the minimum value between the last two steps.
        return min(prev1, prev2)

# Input: cost = [10, 15, 20]
def main():
    cost = [10, 15, 20]
    solution = Solution()
    result = solution.minCostClimbingStairs(cost)
    print(result)
