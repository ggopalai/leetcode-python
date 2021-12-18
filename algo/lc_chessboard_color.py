"""
Black squares sum up to even numbers.
"""
def squareIsWhite(self, coordinates: str) -> bool:
        if (ord(coordinates[0]) + int(coordinates[1])) % 2 == 0:
            return False
        
        return True


"""
Faster solution according to LC - 
"""
def squareIsWhite(self, coordinates: str) -> bool:
        Value = coordinates
        if (Value[0] in ["a", "c", "e", "g"] and Value[1] in ["1", "3", "5", "7"]) or (Value[0] in ["b", "d", "f", "h"] and Value[1] in ["2", "4", "6", "8"]):
            return False
        else:
            return True 