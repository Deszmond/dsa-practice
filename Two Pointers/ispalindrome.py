class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Pattern: Two Pointers (String Filtering)
        # Key Idea: Skip non-alphanumeric characters while comparing inward
        # Time: O(n)
        # Space: O(1)

        l = 0
        r = len(s)-1

        while l < r:
            while l < r and s[l].isalnum() == False:
                l +=1
            while l < r and s[r].isalnum() == False:
                r -=1
            
            if s[l].lower() != s[r].lower():
                return False

            l+=1
            r-=1

        return True