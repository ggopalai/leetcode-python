def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        f = s = t = ""
        for i in firstWord:
            f += str(ord(i) - 97)
        
        for i in secondWord:
            s += str(ord(i) - 97)
            
        for i in targetWord:
            t += str(ord(i) - 97)
            
        f = int(f)
        s = int(s)
        t = int(t)
        
        if f + s == t:
            return True
        
        return False