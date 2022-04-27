"""
Runtime: 28 ms, faster than 82.90% of Python3 online submissions for Sorting the Sentence.
Memory Usage: 14.4 MB, less than 15.73% of Python3 online submissions for Sorting the Sentence.
"""
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        mapping = dict()
        for i in words:
            c = len(i) - 1
            mapping[i[c]] = i[:c]
        
        res = ''
        for i in range(len(words)):
            res = res + f'{mapping[str(i+1)]} ' 
            
        return res.rstrip()
        