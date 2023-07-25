# Title: N-th Tribonacci Numbers
# The Tribonacci sequence Tn is defined as follows:
#
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.

class Solution:
    def tribonacci(self, n: int) -> int:
        # Handle the base cases when n is 0, 1, or 2.
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        # Create an array to store the intermediate Tribonacci numbers.
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = dp[2] = 1

        # Calculate the Tribonacci numbers from 3 up to n using dynamic programming.
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        # Return the n-th Tribonacci number.
        return dp[n]

# Input: n = 6
def main():
    n = 6
    solution = Solution()
    result = solution.tribonacci(n)
    print(result)
