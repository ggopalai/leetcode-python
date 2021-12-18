"""
https://leetcode.com/problems/unique-email-addresses/
"""
def numUniqueEmails(self, emails: List[str]) -> int:
        ue = set()
        for i in emails:
            if '.' in i:
                second = i[i.index('@'):]
                i = i.replace('.','')
                i = i[:i.index('@')] + second
            if '+' in i:
                latter = i[:i.index('+')]
                former = i[i.index('@'):]
                i = latter + former
            ue.add(i)
        
        return len(ue)