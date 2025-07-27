class Solution:
    def setMatrixZeroes(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        first_row = any(mat[0][j] == 0 for j in range(m))
        first_col = any(mat[i][0] == 0 for i in range(n))
        
        # Use first row and column to mark zero positions
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0
        
        # Set matrix cells to zero based on marks
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
        
        # Set first row to zero if needed
        if first_row:
            for j in range(m):
                mat[0][j] = 0
        
        # Set first column to zero if needed
        if first_col:
            for i in range(n):
                mat[i][0] = 0
