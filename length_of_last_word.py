

s = "   fly me   to   the moon  "

class Solution:
    def lengthOfLastWord(self, s):
        i, length = len(s) - 1, 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length


so = Solution()
print(so.lengthOfLastWord(s))

given_array = [1, 2, 3]

for i in given_array:
    print(i)
