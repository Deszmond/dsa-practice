class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # Pattern: reverse traversal (right-to-left scan)
        # Time Complexity: O(k+m) -> O(n), k = trailing spaces, m = last word length
        # Space Complexity

        p = len(s)-1
        count = 0

        while p>=0 and s[p] == " ":
            p -=1

        while p >=0 and s[p] != " ":
            count +=1
            p -=1

        return count
