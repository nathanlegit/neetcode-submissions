class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        target_row = -1
        while top <= bottom:
            mid = (top + bottom)//2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                target_row = mid
                break
            elif target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
        if target_row == -1:
            return False
        left = 0
        right = len(matrix[target_row]) -1
        while left <= right:
            mid = (left + right)//2
            if target == matrix[target_row][mid]:
                return True
            elif target >= matrix[target_row][mid]:
                left = mid + 1
            elif target <= matrix[target_row][mid]:
                right = mid - 1
        return False

