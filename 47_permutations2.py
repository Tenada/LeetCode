from itertools import permutations

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        premutations_set = set(permutations(nums, r = None))
        permutations_list = [list(collection) for collection in premutations_set]
        return permutations_list

nums = [1,1,2]
solution = Solution()
print(solution.permuteUnique(nums))