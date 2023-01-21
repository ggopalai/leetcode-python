class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            # get the ith bit from the left
            bit = (n >> i) & 1
            
            # inserting that bit the result (31 - i controls the reverse position)
            res = res | bit << (31 - i)
        
        return res