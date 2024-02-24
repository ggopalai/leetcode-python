class FrontMiddleBackQueue:
    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        n = len(self.queue)
        idx = n // 2
        self.queue.insert(idx, val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        return self.queue.pop(0) if self.queue else -1

    def popMiddle(self) -> int:
        n = len(self.queue)
        if n == 0:
            return -1
        idx = n // 2 if n % 2 != 0 else (n // 2) - 1
        ele = self.queue.pop(idx)
        return ele 

    def popBack(self) -> int:
        if len(self.queue) == 0:
            return -1
        ele = self.queue[-1]
        self.queue = self.queue[:-1]
        return ele


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()