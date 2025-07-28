#Make Matrix Beautiful
class Solution:
    def balanceSums(self, mat):
        m = len(mat)      # number of rows
        n = len(mat[0])   # number of columns
        
        row_sum = [sum(row) for row in mat]
        col_sum = [sum(mat[i][j] for i in range(m)) for j in range(n)]
        
        # The target sum for each row and column
        target = max(max(row_sum), max(col_sum))
        
        total_operations = 0
        
        # The total number of operations needed is the sum of (target - each row sum)
        for i in range(m):
            total_operations += target - row_sum[i]
        
        return total_operations
