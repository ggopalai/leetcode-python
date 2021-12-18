def sumOfUnique(self, nums: List[int]) -> int:
        res = 0
        t = dict()
        
        for i in nums:
            if i not in t.keys():
                t[i] = 1
            else:
                t[i] += 1
                
        for i in t.items():
            if i[1] == 1:
                res += i[0]
            
        return res