class Bucket():
    def __init__(self):
        self.arr = []
    
    def get(self, key):
        for k, v in self.arr:
            if k == key:
                return v
        
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.arr):
            if kv[0] == key:
                self.arr[i] = (key, value)
                return
        
        self.arr.append((key, value))
    
    def delete(self, key):
        for i, o in enumerate(self.arr):
            if o[0] == key:
                del self.arr[i]
                
        

class MyHashMap(object):

    def __init__(self):
        self.mod = 2069
        self.space = [Bucket() for i in range(self.mod)]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hk = key % self.mod
        self.space[hk].update(key, value)
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hk = key % self.mod
        return self.space[hk].get(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hk = key % self.mod
        self.space[hk].delete(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)