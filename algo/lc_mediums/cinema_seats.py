class Solution:
    """
    Time complexity - linear 
    Space complexity - linear 
    """
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        from collections import defaultdict
        
        seats = defaultdict(set)
        
        # max possible
        count = 2 * n

        for i, j in reservedSeats:
            if j in {4, 5}:
                seats[i].add(0)
                seats[i].add(1)
            
            elif j in {6, 7}:
                seats[i].add(1)
                seats[i].add(2)
            
            elif j in {8, 9}:
                seats[i].add(2)
            
            elif j in {2, 3}:
                seats[i].add(0)
        
        # O(n)
        for i in seats:
            if len(seats[i]) == 3:
                count -= 2
            else:
                count -= 1

        return count
        