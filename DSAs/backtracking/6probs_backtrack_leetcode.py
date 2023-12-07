# Iterative DFS solutions

# 39. Combination Sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        res = []
        candidates.sort()
        def dfs(idx, path, cur):
            if cur > target: return
            if cur == target:
                res.append(path)
                return
            for i in range(idx, len(candidates)):
                dfs(i, path+[candidates[i]], cur+candidates[i])
        dfs(0, [], 0)
        return res
# 40. Combination Sum II

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(idx, path, cur):
            if cur > target: return
            if cur == target:
                res.append(path)
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                dfs(i+1, path+[candidates[i]], cur+candidates[i])
        dfs(0, [], 0)
        return res
# 78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(idx, path):
            res.append(path)
            for i in range(idx, len(nums)):
                dfs(i+1, path+[nums[i]])
        dfs(0, [])
        return res
# 90. Subsets II

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(idx, path):
            res.append(path)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, path+[nums[i]])
        dfs(0, [])
        return res
# 46. Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(counter, path):
            if len(path) == len(nums):
                res.append(path)
                return
            for x in counter:
                if counter[x]:
                    counter[x] -= 1
                    dfs(counter, path+[x])
                    counter[x] += 1
        dfs(Counter(nums), [])
        return res
# 47. Permutations II

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(counter, path):
            if len(path) == len(nums):
                res.append(path)
                return
            for x in counter:
                if counter[x]:
                    counter[x] -= 1
                    dfs(counter, path+[x])
                    counter[x] += 1
        dfs(Counter(nums), [])
        return res