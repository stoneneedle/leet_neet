# nums = [1,1,1,2,2,3]
nums = [1,1,1,2,2,3]

class Solution:
    def removeDuplicates(self, nums):
        l,r = 0, 0

        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1

            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l





s = Solution()
print(s.removeDuplicates(nums))
