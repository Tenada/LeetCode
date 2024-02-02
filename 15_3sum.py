from itertools import combinations

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        all_triplets = combinations(nums, 3)
        zero_triplets = {tuple(sorted(triplet)) for triplet in all_triplets if sum(triplet)==0}
        distinct_triplets = [list(triplet) for triplet in zero_triplets]

        # Empty list is false.
        return distinct_triplets


solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
#nums = [0, 0, 0, 0]

print(solution.threeSum(nums))