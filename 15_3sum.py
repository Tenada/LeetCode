from itertools import combinations

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        all_triplets = combinations(nums, 3)
        zero_triplets = [list(triplet) for triplet in all_triplets if sum(triplet)==0]

        if not zero_triplets: # Empty list is false.
            return zero_triplets

        distinct_triplets = []

        # Вариант 1. Проверить, будут ли все комбинации одного списка равны всем комбинациям другого.
        # Вариант 2. Проверить, найдутся ли числа из одного списка в другом.внутренний списрк нельзя захешировать.
        # Напомню, что
        # [[-1, 0, 1], [-1, 2, -1], [0, 1, -1]]

        for triplet in zero_triplets:
            distinct_triplets.append(triplet)

        return distinct_triplets


solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
#nums = [0, 1, 1]

print(solution.threeSum(nums))