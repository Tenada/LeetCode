import itertools

class Solution(object):
    def permute(self, nums):
        return list(itertools.permutations(nums, r = None))

nums = [1, 3, 5, 8]
solution = Solution()
print(solution.permute(nums))