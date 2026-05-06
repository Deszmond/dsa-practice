class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Problem: Strings (Horizontal Scanning)
        # Thought Process: Compare characters index-by-index across all strings using the first string as reference; stop at first mismatch
        # Time Complexity: O(n * m), n = number of strings, m = length of first string
        # Space Complexity: O(1), only storing the result
        
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res   