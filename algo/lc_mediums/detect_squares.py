class DetectSquares:
    from collections import defaultdict

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        """
        Look for diagonals, then for the other 2 points.
        """
        x, y = point
        count = 0
        
        for xd, yd in self.points:
            if abs(x - xd) == abs(y - yd) and abs(x - xd) > 0:
                count += self.points[(xd, yd)] * self.points[(xd, y)] * self.points[(x, yd)]        
        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)