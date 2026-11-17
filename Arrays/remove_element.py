from typing import List


class Solution:
    # LeetCode 27: Remove Element
    #
    # Problem:
    # Remove all occurrences of val in-place and return the
    # number of remaining elements. Order does not matter.
    #
    # Thought Process:
    # Use two pointers:
    # i = current index being checked.
    # n = exclusive end of the valid array.
    #
    # When nums[i] == val, replace it with the last element
    # in the valid region and shrink that region.
    #
    # Do NOT increment i after replacement because the
    # swapped-in element has not been checked yet.
    #
    # Pattern: Two Pointers / In-Place Array Modification
    #
    # Time Complexity: O(n)
    # Each iteration either advances i or decreases n.
    #
    # Space Complexity: O(1)
    # Only two integer variables are maintained.

    def removeElement(self, nums: List[int], val: int) -> int:

        n = len(nums)
        i = 0

        while i < n:
            if nums[i] == val:

                # Replace unwanted value with the last element
                # in the currently valid region.
                nums[i] = nums[n - 1]

                # Shrink the valid region.
                # Keep i unchanged to inspect the replacement.
                n -= 1
            else:
                # Current element is valid, so move forward.
                i += 1

        # Only nums[:n] contains the retained elements.
        # Values beyond n are irrelevant.
        return n