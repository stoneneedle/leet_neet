nums = [2,3,1,1,4]

class Solution:
    def jump(self, nums):
        ### INIT VARS

        jumps = [] # number of jumps required
        n = len(nums)-1 # reach this index
        jump_lens = []
        i = 0
        jump_count = 0

        ### MAIN PROGRAM (ATTEMPT 2)
        while i < n:
            j = 1

            while j <= nums[i]:
                jump_count += 1
                j += 1
            i += 1

        return jump_count




s = Solution()
print(s.jump(nums))

### ATTEMPT 1
# for i in range(len(nums)):
#     jumps = []
#     j = 1
#     while j < goal: # for j in range(nums[i]):
#         n = i + j if i + j < len(nums)-1 else len(nums)-1
#         jumps.append(nums[n])
#         j += nums[n]
#     jump_lens.append(len(jumps))