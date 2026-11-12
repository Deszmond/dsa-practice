class Solution:
    # Problem: Length of Last Word
    #
    # Thought Process:
    # Start from the end of the string because we only care
    # about the final word.
    #
    # 1. Skip any trailing spaces.
    # 2. Count characters until reaching a space or the
    #    beginning of the string.
    #
    # Pattern: Reverse Traversal / Two-Phase Linear Scan
    #
    # Time Complexity: O(k + m) -> O(n)
    # k = number of trailing spaces
    # m = length of the last word
    # n = total length of the string
    #
    # Space Complexity: O(1)
    # Only two integer variables are maintained.

    def lengthOfLastWord(self, s: str) -> int:

        # Start at the final character (zero-based indexing).
        p = len(s)-1
        count = 0

        # Skip trailing spaces to locate the last word.
        # p >= 0 prevents accessing indices before the string.
        while p>=0 and s[p] == " ":
            p -=1

        # Count characters until reaching a word boundary.
        # This also handles strings containing only one word.
        while p >=0 and s[p] != " ":
            count +=1
            p -=1

        return count