from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        answer = []

        for word in words:
            ptow = {}
            wtop = {}
            matched = True

            for p, w in zip(pattern, word):
                if p not in ptow and w not in wtop:
                    ptow[p] = w
                    wtop[w] = p
                else:
                    if p in ptow and ptow[p] != w:
                        matched = False
                        break
                    if w in wtop and wtop[w] != p:
                        matched = False
                        break

            if matched:
                answer.append(word)

        return answer
