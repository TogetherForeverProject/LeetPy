class Solution:
    def matrixMultiply(self, a, b):
        # Function to perform matrix multiplication
        return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

    def matrixPower(self, matrix, n):
        # Function to calculate the power of a matrix using binary exponentiation
        result = [[1, 0], [0, 1]]  # Identity matrix
        while n > 0:
            if n % 2 == 1:
                result = self.matrixMultiply(result, matrix)
            matrix = self.matrixMultiply(matrix, matrix)
            n //= 2
        return result

    def fib(self, n: int) -> int:
        # Calculate the n-th Fibonacci number using matrix exponentiation with memoization
        if n == 0:
            return 0
        matrix = [[1, 1], [1, 0]]  # Fibonacci matrix
        result_matrix = self.matrixPower(matrix, n - 1)  # Calculate the power of the Fibonacci matrix
        return result_matrix[0][0]  # Return the n-th Fibonacci number


# Input: n = 2
def main():
    n = 2
    solution = Solution()
    result = solution.fib(n)
    print(result)
