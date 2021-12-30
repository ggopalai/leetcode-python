# https://leetcode.com/problems/flipping-an-image/

def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = list()
        for i in image:
            res.append(reversed(i))
        
        temp = list()
        for i in res:
            yo = list()
            for j in i:
                if j == 1:
                    yo.append(0)
                else:
                    yo.append(1)
            temp.append(yo)
        
        return temp