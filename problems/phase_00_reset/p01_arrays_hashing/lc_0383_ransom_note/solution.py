class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_d = {}
        m_d = {}

        for ch in ransomNote:
            if ch in r_d:
                r_d[ch] += 1
            else:
                r_d[ch] = 1

        for ch in magazine:
            if ch in m_d:
                m_d[ch] += 1
            else:
                m_d[ch] = 1

        for k, v in r_d.items():
            if k in m_d:
                if v > m_d[k]:
                    return False
            else:
                return False

        return True
