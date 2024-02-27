import itertools

class Solution(object):
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """
        LeetCode № 1.
        Returns indices of the two numbers which add up to target.
        """
        enums = enumerate(nums)
        for key_1, value_1 in enums:
            for key_2, value_2 in enums:
                if (key_1 != key_2) and (value_1 + value_2 == target):
                    return [key_1, key_2]

    def length_of_longest_substring(self, s: str) -> int:
        """
        LeetCode № 3.
        Returns the length of the longest substring in a given string.
        """
        length = len(s)
        if length == 1:
            return 1

        longest = 0
        unrepeated = []
        counter = 0 # Starting character for current iteration.
        iterated = 0 # Total iterated characters.

        # Iterate the string while characters don't repeat.
        # If one is repeating, update variable "longest".
        # Iterate again from the next character the previous iteration started with.
        while (counter < length):
            character = s[counter]

            if character not in unrepeated:
                unrepeated.append(character)
            else:
                if len(unrepeated) > longest:
                    longest = len(unrepeated)

                unrepeated.clear()
                counter = iterated
                iterated += 1

            counter += 1

        return max(longest, len(unrepeated))

    def median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        LeetCode № 4.
        Returns the middle number in two merged sorted lists.
        """
        nums = sorted(nums1 + nums2)
        length = len(nums)
        half = length // 2

        if length % 2 != 0: # Odd.
            return float(nums[half])
        else: # Even.
            return float(nums[half] + nums[half - 1]) / 2

    def is_palindrome(self, x: int) -> bool:
        """
        LeetCode № 9.
        Returns if int is a palindrome.
        """
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

    def permute(self, nums: list[int]) -> list[int]:
        """
        LeetCode № 46.
        Returns all the possible permutations of a list.
        The list contains distinct numbers only.
        """
        return list(itertools.permutations(nums, r = None))

    def permute_unique(self, nums: list[int]) -> list[list[int]]:
        """
        LeetCode № 47.
        Returns all the unique permutations of the list.
        The list may contain duplicates.
        """
        unique = set(itertools.permutations(nums, r = None))
        permutations_list = [list(collection) for collection in unique]
        return permutations_list
    
    def can_jump(self, nums: list[int]) -> bool:
        """
        LeetCode № 55.
        Returns if the end of the list is reachable.
        List value is the length of 'jump'.
        """
        reachable = 0
        for index, jump in enumerate(nums):
            if index+jump >= reachable:
                 reachable = index+jump

            # One can reach here, but not further.
            if index == reachable:
                break
            
        return reachable >= len(nums) - 1
    
    def getPermutation(self, n: int, k:int) -> str:
        """
        LeetCode № 60.
        Returns k-th permutation of a list made of range(1, n+1).
        """
        permutation_sequence = list(itertools.permutations(range(1, n+1)))
        permutation_tuple = permutation_sequence[k-1]
        permutation_string = "".join(str(element) for element in permutation_tuple)
        return permutation_string