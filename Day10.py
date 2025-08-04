
class Solution:
    def maxRectSum(self, mat):
        if not mat or not mat[0]:
            return 0

        n, m = len(mat), len(mat[0])
        max_sum = float('-inf')

        for left in range(m):
            temp = [0] * n  # Initialize the temporary array
            for right in range(left, m):
                # Add the current column values to each row
                for i in range(n):
                    temp[i] += mat[i][right]

                # Apply Kadane's Algorithm to temp
                current_sum = self.kadane(temp)
                max_sum = max(max_sum, current_sum)

        return max_sum

    def kadane(self, arr):
        max_end_here = max_so_far = arr[0]
        for num in arr[1:]:
            max_end_here = max(num, max_end_here + num)
            max_so_far = max(max_so_far, max_end_here)
        return max_so_far
