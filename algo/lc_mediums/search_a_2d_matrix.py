class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        cols = len(matrix[0])
        rows = len(matrix)
        while row < rows and target > matrix[row][cols - 1]:
            row += 1
        if row == rows:
            return False
        
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
            