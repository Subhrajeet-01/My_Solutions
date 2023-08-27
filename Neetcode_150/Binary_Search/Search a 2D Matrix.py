class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        return False

                 # USING BINARY SEARCH 

        """
        def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
        """
