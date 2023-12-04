from typing import List

class Solution:
    def permute_helper(self, candidate, nums, res):
        if not nums:
            res.append(candidate.copy())
            return
        for i in range(len(nums)):
            cur_choice = nums[i]
            self.permute_helper(candidate + [cur_choice], nums[:i] + nums[i+1:], res)

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.permute_helper([], nums, res)
        return res

print(Solution().permute([1,2,3]))
