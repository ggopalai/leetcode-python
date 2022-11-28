class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        all_players = []
        lc = collections.defaultdict(int)
        for w, l in matches:
            all_players.extend([w, l])
            lc[l] += 1
        
        res = []
        zl, ol = [], []
        for k, v in lc.items():
            if v == 1:
                ol.append(k)
        
        zl = set(all_players).difference(set(lc.keys()))
        
        res.append(sorted(zl))
        res.append(sorted(ol))
        
        return res
            