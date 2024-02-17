class Solution(object):
    def lengthOfLongestSubstring(self, s) -> int:
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 1:
            return 1

        longest = 0
        unrepeated = []
        counter = 0 # Starting character for current iteration.
        iterated = 0 # Total number of iterated symbols starting from the left.

        while (counter < length):
            character = s[counter]

            if character not in unrepeated:
                unrepeated.append(character)
            else:
                if len(unrepeated) > longest:
                    longest = len(unrepeated)

                # Now iteration starts with the character next to the one the previous iteration started with.
                unrepeated.clear()
                counter = iterated
                iterated += 1

            counter += 1

        return max(longest, len(unrepeated))

solution = Solution()
s = "jbpnbwwd"
print(solution.lengthOfLongestSubstring(s))