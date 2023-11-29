class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # idx, height
        maxArea = 0

        for i, h in enumerate(heights):
            # start tracks how backward it can be extended
            start = i

            # pop because we cannot extend ahead
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx)) # (excludes current bar)
                start = idx

            stack.append((start, h))
        
        # these are the ones which could be extended all the way to the end.
        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
        
        return maxArea
