# quadratic time, constant space. 
# rotate outer square, then move inwards.
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        
        # to set outer boundaries
        while l < r:
            # other positions of the outer squares
            for i in range(r - l):
                top, bottom = l, r
                
                # save top left
                temp = matrix[top][l + i]
                
                # set top left to bottom left
                matrix[top][l + i] = matrix[bottom - i][l]
                
                # set bottom left to bottom right
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                # set bottom right to top right
                matrix[bottom][r - i] = matrix[top + i][r]
                
                # set top right to top left.
                matrix[top + i][r] = temp
            
            l += 1
            r -= 1