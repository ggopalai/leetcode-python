class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        store = collections.defaultdict(int)
        
        for i in cpdomains:
            n, sd = i.split(' ')
            n = int(n)
            d = sd.split('.')
            
            if len(d) == 2:
                store[f'{d[0]}.{d[1]}'] += n
                store[d[1]] += n
            else:
                store[f'{d[0]}.{d[1]}.{d[2]}'] += n
                store[f'{d[1]}.{d[2]}'] += n
                store[d[2]] += n
        
        res = []
        for k, v in store.items():
            res.append(f'{v} {k}')
        
        return res