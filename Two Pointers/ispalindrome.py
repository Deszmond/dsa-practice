class Solution:
    # LeetCode 125: Valid Palindrome
    #
    # Problem:
    # Determine whether a string reads the same forwards
    # and backwards, ignoring non-alphanumeric characters
    # and differences in letter case.
    #
    # Thought Process:
    # Use two pointers at opposite ends of the string.
    # Skip non-alphanumeric characters independently.
    # Compare the remaining characters case-insensitively.
    # Move both pointers inward after each successful match.
    #
    # Pattern: Two Pointers / Inward Traversal
    #
    # Time Complexity: O(n)
    # Each pointer moves inward and never revisits a position.
    #
    # Space Complexity: O(1) auxiliary space
    # No filtered string or character array is created.
    #
    # Key Insight:
    # Filter characters during traversal rather than
    # preprocessing the entire string.

    def isPalindrome(self, s: str) -> bool:

        # Initialise pointers at opposite ends.
        l = 0
        r = len(s)-1

        while l < r:

            # Skip non-alphanumeric characters from the left.
            # The boundary check prevents the pointers crossing.
            while l < r and s[l].isalnum() == False:
                l +=1

            # Skip non-alphanumeric characters from the right.
            while l < r and s[r].isalnum() == False:
                r -=1

            # Compare characters without case sensitivity.
            # A mismatch immediately disproves the palindrome.
            if s[l].lower() != s[r].lower():
                return False

            # Both characters matched; move inward.
            l+=1
            r-=1

        # All required character pairs matched.
        return True