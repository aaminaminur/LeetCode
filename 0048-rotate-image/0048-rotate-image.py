class Solution:
    def transpose(self, matrix: List[List[int]]):
        for i in range(len(matrix)):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def reverse_rows(self, row: List[int]):
        low = 0
        high = len(row) - 1
        while low<high:
            row[low], row[high] = row[high], row[low]
            low += 1
            high -= 1
        return row
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # get the transpose
        self.transpose(matrix)
        # reverse the rows
        for i in range(len(matrix)):
            matrix[i] = self.reverse_rows(matrix[i])
