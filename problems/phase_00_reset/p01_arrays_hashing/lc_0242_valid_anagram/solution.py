class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic_s = {}
        dic_t = {}

        for ch in s:
            if ch in dic_s:
                dic_s[ch] += 1
            else:
                dic_s[ch] = 1

        for ch in t:
            if ch in dic_t:
                dic_t[ch] += 1
            else:
                dic_t[ch] = 1

        return dic_s == dic_t
