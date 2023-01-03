class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        nwords = len(strs)
        m = len(strs[0])
        count = 0
        
        # outer loop to index current column
        for i in range(m):
            # inner loop to index words
            for j in range(nwords - 1):
                if strs[j][i] > strs[j+1][i]:
                    count += 1
                    break
        
        return count 