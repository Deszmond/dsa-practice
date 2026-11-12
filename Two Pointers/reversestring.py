from typing import List


class Solution:
    # LeetCode 344: Reverse String
    #
    # Problem:
    # Reverse an array of characters in-place without
    # allocating another array or returning a result.
    #
    # Thought Process:
    # Initialise two pointers at opposite ends.
    # Swap their elements, then move both pointers inward.
    # Continue until the pointers meet or cross.
    #
    # Pattern: Two Pointers / In-Place Reversal
    #
    # Time Complexity: O(n)
    # Each iteration processes two positions.
    # Approximately n/2 swaps are performed.
    #
    # Space Complexity: O(1) auxiliary space
    # Swapping uses constant additional memory.
    # The original list is modified directly.
    #
    # Key Insight:
    # Swapping symmetric positions reverses the list
    # without requiring a second array.

    def reverseString(self, s: List[str]) -> None:

        """
        Do not return anything, modify s in-place instead.
        """

        # Last valid index of the array.
        n = len(s)-1

        # Initialise pointers at opposite ends.
        R = n
        L = 0

        # Stop when pointers meet or cross.
        # The middle element of an odd-length array
        # does not need to be swapped.
        while R > L:

            # Swap the two characters directly in the list.
            s[R],s[L] = s[L],s[R]

            # Move both pointers toward the centre.
            L +=1
            R -=1

        # ISSUE: LeetCode expects no return value.
        # The array is already reversed in-place.
        return s