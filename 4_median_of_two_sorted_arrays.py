class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        nums = sorted(nums1 + nums2)
        length = len(nums)
        half = length // 2

        if length % 2 != 0: # Odd.
            return float(nums[half])
        else: # Even.
            return float(nums[half] + nums[half - 1]) / 2

solution = Solution()
print(solution.findMedianSortedArrays([1, 2], [4, 3]))