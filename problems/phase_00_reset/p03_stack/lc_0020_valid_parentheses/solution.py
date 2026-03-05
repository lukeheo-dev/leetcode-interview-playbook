class Solution:
    def isValid(self, s: str) -> bool:
        opens = []

        if s[0] in "})]":
            return False
        elif s[-1] in "({[":
            return False

        for ch in s:
            if ch in "({[":
                opens.append(ch)
            elif ch == ")":
                if len(opens) != 0 and opens[-1] == "(":
                    opens.pop()
                else:
                    return False
            elif ch == "]":
                if len(opens) != 0 and opens[-1] == "[":
                    opens.pop()
                else:
                    return False
            elif ch == "}":
                if len(opens) != 0 and opens[-1] == "{":
                    opens.pop()
                else:
                    return False

        return len(opens) == 0
