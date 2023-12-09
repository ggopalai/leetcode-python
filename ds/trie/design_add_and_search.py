class TrieNode:
    def __init__(self):
        self.dict = {}
        self.ends = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c in cur.dict:
                cur = cur.dict[c]
            else:
                cur.dict[c] = TrieNode()
                cur = cur.dict[c]
        cur.ends = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i] 
                
                #backtrack
                if c == '.':
                    for child in cur.dict.values():
                        if dfs(i + 1, child):
                          return True
                    return False 
                
                # normal scenario
                else:
                    if c in cur.dict:
                        cur = cur.dict[c]                    
                    else:
                        return False 
            
            return cur.ends
        
        return dfs(0, self.root)

    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)