nums = [1,2,1]

class Solution:
    def getConcatenation(self, nums):
        ans = []
        for i in range(len(nums)*2):
            w = i if i < len(nums) else i - len(nums)
            ans.append(nums[w])
        return ans


s = Solution()
print(s.getConcatenation(nums))