class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        r = len(nums)

        from collections import defaultdict
        d = defaultdict(list)

        for i in range(r):
            for j in range(len(nums[i])):
                d[i+j].append(nums[i][j])
                
        res = []
        for _, v in d.items():
            res.extend(reversed(v))
        
        return res


        