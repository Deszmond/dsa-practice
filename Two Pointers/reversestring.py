class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        # Pattern: Two Pointers (In-place reversal)
        # Key Idea: Swap elements from both ends moving inward
        # Time: O(n)
        # Space: O(1)
        # In-place operation: modifies input array directly without extra storage

        n = len(s)-1
        R = n
        L = 0

        while R > L:
            s[R],s[L] = s[L],s[R]
            L +=1
            R -=1

        return s
        
        """
        Do not return anything, modify s in-place instead.
        """
        