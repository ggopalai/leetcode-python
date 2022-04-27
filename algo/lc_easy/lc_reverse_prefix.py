# https://leetcode.com/problems/reverse-prefix-of-word/

def reversePrefix(self, word: str, ch: str) -> str:
        a = word.find(ch)
        if a == -1:
            return word
        
        return word[0: a+1][::-1] + word[a+1:]