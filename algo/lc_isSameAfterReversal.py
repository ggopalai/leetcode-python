class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == int(str(int(str(num)[::-1]))[::-1]):
            return True
        else:
            return False