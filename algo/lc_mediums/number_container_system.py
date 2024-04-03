from collections import defaultdict
import bisect 

class NumberContainers:
    def __init__(self):
        self.idxVal = defaultdict(int)
        self.valIdx = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        oldVal = self.idxVal.get(index, None)
        
        if oldVal is not None:
            self.valIdx[oldVal].remove(index)
            if not self.valIdx[oldVal]:
                del self.valIdx[oldVal]
        
        self.idxVal[index] = number
        bisect.insort(self.valIdx[number], index)

    def find(self, number: int) -> int:
        return self.valIdx.get(number, [-1])[0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)