# Title: Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Eachtime you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n):
        # Base cases: If n is 0 or 1, there's only one way to climb.
        if n == 0 or n == 1:
            return 1

        # Initialize variables to store the number of ways to reach the current step
        # (prev1) and the previous step (prev2).
        prev1, prev2 = 1, 1

        # Calculate the number of ways to reach each step from 2 to n.
        for _ in range(2, n + 1):
            # Calculate the number of ways to reach the current step by adding the ways
            # to reach the previous two steps (prev1 and prev2).
            current = prev1 + prev2

            # Update prev1 and prev2 for the next iteration.
            prev1, prev2 = prev2, current

        # The number of ways to reach the top of the staircase (n steps) is stored in prev2.
        return prev2

# Input: num_steps = 4
def main():
    sol = Solution()
    num_steps = 4
    distinct_ways = sol.climbStairs(num_steps)
    print(distinct_ways)
