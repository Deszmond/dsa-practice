from typing import List


class Solution:
    # Problem: Longest Common Prefix
    #
    # Thought Process:
    # Use the first string as a reference.
    # Compare each character position across all strings.
    # Stop immediately when a string ends or a mismatch occurs.
    #
    # Pattern: Vertical Scanning / String Comparison
    #
    # Time Complexity: O(n * m + m^2)
    # n = number of strings
    # m = length of the first string
    # The nested loops perform up to O(n * m) comparisons.
    # Repeated string concatenation can add O(m^2) work.
    #
    # Space Complexity: O(m)
    # The result string can grow to the length of the first string.

    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""

        # Check each character position in the first string.
        for i in range(len(strs[0])):

            # Every string must contain the same character at i.
            for s in strs:

                # Check the boundary BEFORE accessing s[i].
                # A shorter string limits the common prefix.
                if i == len(s) or s[i] != strs[0][i]:
                    return res

            # Only append after ALL strings match at index i.
            res += strs[0][i]

        return res