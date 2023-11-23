"""
Monotonic stack (increasing)
Time - O(n)
Space - O(n)
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted(zip(position, speed))
        
        time = [(target - p)/s for p, s in pairs]

        stack.append(time[-1])
        for i in range(len(time) - 1, -1, -1):
            if time[i] > stack[-1]:
                stack.append(time[i])
        
        return len(stack)
        