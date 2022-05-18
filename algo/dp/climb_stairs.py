class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        steps = list()
        steps.extend([0, 1, 2])
        for i in range(3, n+1):
            steps.append(steps[i-1] + steps[i-2])
        
        return steps[-1]

# a better solution -> don't need to store everything. just need previous two values. problem reduces to fibanocci sequence. 