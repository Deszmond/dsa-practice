class Solution:
    # LeetCode 392: Is Subsequence
    #
    # Problem:
    # Determine whether string s is a subsequence of string t.
    # Characters must appear in the same relative order,
    # but they do not need to be adjacent.
    #
    # Thought Process:
    # Use two pointers to track positions in s and t.
    # Traverse t, searching for each character of s in order.
    #
    # If characters match, advance both pointers.
    # Otherwise, advance only the pointer in t.
    #
    # Pattern: Two Pointers / Greedy Subsequence Matching
    #
    # Time Complexity: O(m)
    # m = len(t), n = len(s).
    # Each iteration advances p_t, so at most m iterations occur.
    # More precisely: O(min(m, n)) in the best matching cases,
    # but O(m) in the worst case.
    #
    # Space Complexity: O(1)
    # Only two integer pointers are maintained.
    #
    # Key Insight:
    # The order of characters matters, not their positions.
    # Greedily matching each character at its earliest available
    # position leaves the most characters in t for future matches.

    def isSubsequence(self, s: str, t: str) -> bool:

        # Track the current character in each string.
        p_s, p_t = 0, 0

        # Stop when either all characters in s have matched
        # or there are no more characters in t to examine.
        while p_s < len(s) and p_t < len(t):

            # Matching characters advance the subsequence pointer.
            if s[p_s] == t[p_t]:
                p_s += 1

            # Always advance through t, even without a match.
            # Unmatched characters in t can be skipped.
            p_t += 1

        # Every character in s must have been matched.
        return p_s == len(s)