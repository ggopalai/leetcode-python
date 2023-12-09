class Solution:
    """
    Time - O(n)
    Space - O(n)
    Former google phone screen question.
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import defaultdict 
	
        # store the seen indices 
        hm = defaultdict(int)
        
        for idx, val in enumerate(nums):
            if val in hm:
                if abs(hm[val] - idx) <= k:
                    return True 
            hm[val] = idx 
        
        return False

        