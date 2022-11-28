class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        #check if array is a line or a rectangle
        if (rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]): return False
        
        return not (rec1[2] <= rec2[0] or #rec1 to the left of rec2
                    rec1[0] >= rec2[2] or #rec2 to the right of rec2
                    rec1[3] <= rec2[1] or #rec1 below rec2
                    rec1[1] >= rec2[3]) #rec1 above rec2 
        