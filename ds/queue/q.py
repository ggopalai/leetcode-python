from collections import deque

class Queue:
    def __init__(self):
        self.q = list()
    
    def eq(self, a):
        self.q.append(a)

    def dq(self):
        if len(self.q) < 1:
            print("empty queue")
        else:
            self.q.pop(0)
    
    def isEmpty(self):
        return len(self.q) == 0
    
    def printQ(self):
        print(self.q)

class DQueue:
    def __init__(self):
        self.q = deque()
    
    def eq(self, a):
        self.q.append(a)

    def dq(self):
        if len(self.q) < 1:
            print("empty queue")
        else:
            self.q.popleft()
    
    def isEmpty(self):
        return len(self.q) == 0
    
    def printQ(self):
        print(self.q)
    
if __name__ == '__main__':
    q = DQueue()
    q.eq(1)
    q.eq(2)
    q.eq(3)
    q.printQ()
    q.dq()
    q.printQ()
    q.eq(10)
    q.printQ()
    q.dq()
    q.printQ()
    print(q.isEmpty())

