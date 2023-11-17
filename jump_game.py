nums = [2,3,1,1,4] # 'winner' (True)
nums = [3,2,1,0,4] # 'loser' (False)

class Solution:
    def canJump(self, nums):
        i = 0

        while i < len(nums)-1:
            steps = []
            for j in range(nums[i]):
                n = i+j if i+j < len(nums)-1 else len(nums)-1
                if nums[n] > 0:
                    steps.append(nums[n])
                else:
                    return False
            if steps:
                choice = max(steps)
            else:
                return False
            index_choice = max(range(len(steps)), key=steps.__getitem__)

            i = index_choice + choice

        return True

s = Solution()
print(s.canJump(nums))