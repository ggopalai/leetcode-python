class Solution:
    """
    Custom sort implementation.
    Time - O(n log n)
    """
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        return sorted(sorted(arr, key = lambda num: abs(x - num))[:k])

# can be optimzed using binary search and two pointers.

# furthur optmization with just a modified binary search.

