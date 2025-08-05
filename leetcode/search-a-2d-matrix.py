class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])

        low, high = 0, rows * cols - 1;

        while low <= high:

            middle = low + (high - low) // 2
            row_num = middle // cols
            col_num = middle % cols
            value = matrix[row_num][col_num]

            if value < target:
                low = middle + 1 
            elif value > target: 
                high = middle - 1
            else:
                return True
        return False