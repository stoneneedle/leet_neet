haystack = "mississippi"
needle = "issipi"

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        # notional solution - produces some kind of error in Leetcode, thus he offers an alternative
        # for i in range(len(haystack) - len(needle) + 1 ):
        #     for j in range(len(needle)):
        #         if haystack[i+j] != needle[j]:
        #             break
        #         if j == len(needle) - 1:
        #             return i
        # return -1

        # Leetcode implementation
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

        # Time complexity: O(n * m)
        # Space complexity: O(1)


s = Solution()
print(s.strStr(haystack, needle))