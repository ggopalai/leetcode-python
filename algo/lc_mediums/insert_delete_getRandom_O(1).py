class RandomizedSet:
    def __init__(self):
        self.hm = collections.defaultdict(int)
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.hm:
            return False 
        self.vals.append(val)
        self.hm[val] = len(self.vals) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hm:
            return False
        idx = self.hm[val]
        li, le = len(self.vals) - 1, self.vals[-1]
        self.vals[idx] = le
        self.hm[le] = idx
        
        self.vals.pop()
        del self.hm[val] 

        return True

    def getRandom(self) -> int:
        return choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()