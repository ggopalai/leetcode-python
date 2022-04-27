class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res = str()
        for i in title.split(' '):
            if len(i) > 2:
                t = i.lower()
                res += f'{t.capitalize()} '
            else:
                res += f'{i.lower()} '
                
        return res[:len(res)-1]