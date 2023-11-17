s = "A man, a plan, a canal: Panama"

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum()).lower()
        same = 0
        palindrome = list(zip(list(s), list(reversed(s))))

        for ch_s, ch_e in palindrome:
            if ch_s == ch_e:
                same += 1

        if same == len(s):
            return True
        return False

so = Solution()
print(so.isPalindrome(s))