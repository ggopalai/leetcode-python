class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = 0
        rows, cols = len(matrix), len(matrix[0])

        def maxAreaLinear(heights: List):
            stack = []
            nonlocal maxArea
            for i, h in enumerate(heights):
                 # start tracks how backward it can be extended
                start = i

                # pop because we cannot extend ahead
                while stack and stack[-1][1] > h:
                    idx, height = stack.pop()
                    maxArea = max(maxArea, height * (i - idx)) # ()excludes current bar)
                    start = idx

                stack.append((start, h))
        
            # these are the ones which could be extended all the way to the end.
            for i, h in stack:
                maxArea = max(maxArea, (len(heights) - i) * h)
            
            return maxArea
        
        # build cumulative histograms 
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if not i:
                    dp[i][j] = 1 if matrix[i][j] == "1" else 0
                else:
                    if matrix[i][j] == "1":
                        dp[i][j] = dp[i - 1][j] + 1
        
        for i in range(rows):
            maxAreaLinear(dp[i])

        return maxArea
        


