#1. Naive, works. But try to optimize. 
from copy import copy


class MyQueue:

    def __init__(self):
        self.s1, self.s2 = [], []    

    def push(self, x: int) -> None:
        self.s1.append(x)
        self.s2 = []
        temp = copy.copy(self.s1)
        while temp:
            self.s2.append(temp.pop())

    def pop(self) -> int:
        res = self.s2.pop()
        self.s2 = []
        temp1 = copy.copy(self.s1[1:])
        temp2 = copy.copy(self.s1[1:])
        while temp1:
            self.s2.append(temp1.pop())
        self.s1 = temp2
        return res
    

    def peek(self) -> int:
        return self.s2[-1]

    def empty(self) -> bool:
        return True if len(self.s1) == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

#2. Without using any temporary copies and second stack as auxiallary stack. (Enq is O(N), dq is O(1))
class MyQueue:

    def __init__(self):
        self.s1, self.s2 = [], []
        

    def push(self, x: int) -> None:
        while(self.s1):
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        
        while(self.s2):
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return True if len(self.s1) == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# 3. eq is O(1), dq costlier but amortized to constant.(peek also becomes more expensive)

class MyQueue:

    def __init__(self):
        self.s1, self.s2 = [], []
        

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2 and self.s1:
            while(self.s1):
                self.s2.append(self.s1.pop())
            return self.s2.pop()
        else:
            return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        else:
            while(self.s1):
                self.s2.append(self.s1.pop())
            temp = self.s2[-1]
            while(self.s2):
                self.s1.append(self.s2.pop())
            return temp
                

    def empty(self) -> bool:
        return True if (len(self.s1) == 0 and len(self.s2) == 0) else False
