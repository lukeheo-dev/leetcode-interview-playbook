from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for st in strs:
            key = "".join(sorted(st))
            if key in dic:
                dic[key].append(st)
            else:
                dic[key] = [st]

        return [dic[k] for k in dic]
