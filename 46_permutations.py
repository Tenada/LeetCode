from itertools import permutations

class Solution(object):
    def permute(self, nums):
        return list(permutations(nums, r = None))

nums = [1, 3, 5, 8]
solution = Solution()
print(solution.permute(nums))