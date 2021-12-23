def destCity(self, paths: List[List[str]]) -> str:
        d = dict()
        for i in paths:
            if i[0] not in d:
                d[i[0]] = 1
            else:
                d[i[0]] += 1
            
            if i[1] not in d:
                d[i[1]] = -1
            else:
                d[i[1]] -= 1
                
        for i in d.items():
            if i[1] == -1:
                return i[0] 