class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        maxElement = max(arr)
        cur = arr[0]
        queue = arr[1:]
        streak = 0
        while queue:
            opponent = queue.pop(0)
            if cur > opponent:
                streak += 1
                queue.append(opponent)
            else:
                queue.append(cur)
                cur = opponent
                streak = 1
            
            if streak == k or cur == maxElement:
                return cur
        
                