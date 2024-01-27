class Solution(object):
    def two_sum(self, nums, target):
        enums = enumerate(nums)
        for key_1, value_1 in enums:
            for key_2, value_2 in enums:
                if (key_1 != key_2) and (value_1 + value_2 == target):
                    return [key_1, key_2]

solution = Solution()
nums = [2, 11, 7, 15]
target = 9

print(solution.two_sum(nums, target))