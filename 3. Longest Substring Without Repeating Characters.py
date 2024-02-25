class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 1:
            return 1

        # Length of the currently longest substring.
        longest = 0

        # Current list of non-repeating characters.
        no_repeat = []

        # Starting character.
        counter = 0

        while (counter < length):
            character = s[counter]

            if character not in no_repeat:
                no_repeat.append(character)
            else:
                if len(no_repeat) > longest:
                    longest = len(no_repeat)
                    del no_repeat[:]
                    no_repeat.append(s[counter-1])
                    counter = counter - 1

            counter += 1

        if len(no_repeat) > longest:
            return len(no_repeat)
        else:
            return longest

solution = Solution()
s = "anviaj"
print(solution.lengthOfLongestSubstring(s))