class Solution:
    def countTime(self, time: str) -> int:
        hh = time[:2]
        mm = time[3:]
        h_count = 0
        m_count = 0

        # hh count
        if hh == '??':
            h_count = 24
        elif hh[0] != '?' and hh[1] == '?':
            if int(hh[0]) in [0, 1]:
                h_count = 10
            else:
                h_count = 4
        elif hh[0] == '?' and hh[1] != '?':
            if int(hh[1]) > 3:
                h_count = 2
            else:
                h_count = 3
        else:
            h_count = 1

        # mm count
        if mm == '??':
            m_count = 60
        elif mm[0] != '?' and mm[1] != '?':
            m_count = 1
        elif mm[0] == '?' and mm[1] != '?':
            m_count = 6
        else:
            m_count = 10
        
        return h_count * m_count