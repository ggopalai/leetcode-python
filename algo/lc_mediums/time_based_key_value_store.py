#Works but times out for large cases. 
class TimeMap:

    def __init__(self):
        self.m = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))
        self.m[key].sort(key = lambda x : x[0], reverse=True)
        # print(self.m)

    def get(self, key: str, timestamp: int) -> str:
        a = self.m[key]
        for i, j in a:
            if i == timestamp or timestamp > i:
                return j
        
        return ""
            
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)