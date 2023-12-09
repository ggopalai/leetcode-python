class TrieNode:
    def __init__(self):
        self.node = {}
        self.ends = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cursor = self.root
        for c in word:
            if c in cursor.node:
                cursor = cursor.node[c]
            else:
                cursor.node[c] = TrieNode()
                cursor = cursor.node[c]
        cursor.ends = True

    def search(self, word: str) -> bool:
        cursor = self.root
        for c in word:
            if c in cursor.node:
                cursor = cursor.node[c]
            else:
                return False
        
        return cursor.ends
    
    def startsWith(self, prefix: str) -> bool:
        cursor = self.root
        for c in prefix:
            if c in cursor.node:
                cursor = cursor.node[c]
            else:
                return False
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)