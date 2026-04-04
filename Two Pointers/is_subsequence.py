lass Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # Pattern: Two Pointers (Greedy subsequence matching)
        # Key idea: Move through t and advance s only when characters match.
        # Time Complexity: O(n + m)
        # Space Complexity: O(1)
        p_s, p_t = 0, 0

        while p_s < len(s) and p_t < len(t):
            if s[p_s] == t[p_t]:
                p_s += 1
            p_t += 1

        return p_s == len(s)
        
