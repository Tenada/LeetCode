from itertools import combinations
from itertools import islice

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        all_triplets = (triplet for triplet in combinations(nums, 3) if sum(triplet)==0)
        zero_triplets = {tuple(sorted(triplet)) for triplet in all_triplets}
        distinct_triplets = [list(triplet) for triplet in zero_triplets]

        # Empty list is false.
        return distinct_triplets #!!


solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
#nums = [0, 0, 0, 0]

print(solution.threeSum(nums))