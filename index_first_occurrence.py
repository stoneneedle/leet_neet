# haystack = "sadbutsad"
# needle = "sad"
# haystack = "leetcode_neetcode"
# needle = "leeto"

haystack = "mississippi"
needle = "issipi"

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                needle_start_pos = i
                for j in range(len(needle)):
                    index_first_occurrence.py
                    if haystack[search] == needle[j]:
                        if j == len(needle)-1:
                            return needle_start_pos
                    else:
                        break
        return -1

s = Solution()
print(s.strStr(haystack, needle))