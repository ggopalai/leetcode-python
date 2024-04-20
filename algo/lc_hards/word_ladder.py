class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        from collections import defaultdict 
        # store a hashmap of pattern -> list of matching word 
        nei = defaultdict(list)
        # n times 
        for word in wordList:
            for j in range(len(word)): # m times
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
        
        # shortest path - bfs 
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for n in nei[pattern]:
                        if n not in visit:
                            visit.add(n)
                            q.append(n)
            res += 1
        
        return 0
        



        
