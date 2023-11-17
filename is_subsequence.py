s = "abc"  # potential subsequence
t = "ahbgdc"  # string to be checked


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        if i == len(s):
            return True
        else:
            return False











        # u = []
        #
        # for c in t:
        #     if c in s:
        #         u.append(c)
        # u = ''.join(u)
        #
        # if u == s:
        #     return True
        # else:
        #     return False



print(Solution().isSubsequence(s, t))
