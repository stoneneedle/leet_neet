# Time: O(n * 2^n), Space: O(n)
def subsets_without_duplicates(choices):
    res = []
    subsets_without_duplicates_helper([], choices, res)
    return res


def subsets_without_duplicates_helper(candidates, choices, res):
    res.append(candidates.copy())
    if not choices:
        return

    for i in range(len(choices)):
        subsets_without_duplicates_helper(candidates + [choices[i]], choices[i+1:], res)

# choices = [1,2,3]
# print(subsets_without_duplicates(choices))

# This is for a subarray with duplicates (called a subset but something of a misnomer,
# as sets don't have duplicates

# Time: O(n * 2^n), Space: O(n)
def subsetsWithDuplicates(nums):
    nums.sort()
    subsets, candidates = [], []
    helper2(0, nums, candidates, subsets)
    return subsets


def helper2(i, nums, candidates, subsets):
    if i >= len(nums):
        subsets.append(candidates.copy())
        return

    # decision to include nums[i]
    candidates.append(nums[i])
    helper2(i + 1, nums, candidates, subsets)
    candidates.pop()

    # decision NOT to include nums[i]
    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        i += 1
    helper2(i + 1, nums, candidates, subsets)

choices = [1,2,2,3]
print(len(subsetsWithDuplicates(choices)))
