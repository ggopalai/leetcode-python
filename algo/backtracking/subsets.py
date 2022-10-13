class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #result list
        res = []
        
        #keep track of the subsets
        s = []
        def dfs(i):

            #base case when we run out of bounds
            if i == len(nums):
                res.append(s.copy())
                return 
            
            #decison to include the ith number
            s.append(nums[i])
            dfs(i + 1)
            
            #decision to exclude the ith number
            s.pop()
            dfs(i + 1)
        
        #start with 0th index. 
        dfs(0)
        return res