class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        def reverse_list(data):
            i = 0
            j = len(data) - 1
            while i<=j:
                data[i], data[j] = data[j], data[i]
                i += 1
                j -= 1 
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for data in matrix:
            reverse_list(data)