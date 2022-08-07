class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = {}
        ts = {}
        print([i for i in zip(s, t)])
        for i, j in zip(s, t):
            if i not in st and j not in ts:
                st[i] = j
                ts[j] = i
            
            if st.get(i) != j or ts.get(j) != i:
                return False
        
        return True