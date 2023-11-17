s = "A man, a plan, a canal: Panama"

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''

        for c in s:
            if c.isalnum():
                newStr += c.lower()

        print(newStr[::-1])

        return newStr == newStr[::-1]

# Issues with solution:
# interviewer may not want you to use extra memory (building a new string),
# and may not want you to use isalnum(), instead implementing it yourself

so = Solution()
print(so.isPalindrome(s))
