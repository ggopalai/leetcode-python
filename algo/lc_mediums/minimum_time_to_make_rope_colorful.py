class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        i = 0

        while i < len(colors) - 1:
            j = i + 1

            # need to burst all adjacent balloons except the max
            while j < len(colors) and colors[j] == colors[i]:
                j += 1

            # found more than 2 same colored balloons
            if j - i > 1:
                res += sum(neededTime[i:j]) - max(neededTime[i:j])
            
            i = j
        
        return res
        