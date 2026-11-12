from typing import List


class Solution:
    # LeetCode 1299: Replace Elements with Greatest Element on Right Side
    #
    # Problem:
    # Replace every element with the greatest element to its right.
    # Replace the final element with -1.
    #
    # Thought Process:
    # Traverse the array from right to left, maintaining the
    # maximum value encountered so far.
    #
    # For each element:
    # 1. Calculate the updated maximum, including the current value.
    # 2. Replace the current element with the previous rightMax.
    # 3. Update rightMax for the next iteration.
    #
    # Pattern: Reverse Traversal / Running Maximum
    #
    # Time Complexity: O(n)
    # Each element is visited exactly once.
    #
    # Space Complexity: O(1) auxiliary space
    # Only two additional variables are maintained.
    # The input array is modified in-place.
    #
    # Key Insight:
    # Save the updated maximum BEFORE overwriting arr[i],
    # but update rightMax AFTER replacing arr[i].
    # This ensures the current element is excluded from
    # its own replacement value.

    def replaceElements(self, arr: List[int]) -> List[int]:

        # Initially, there are no elements to the right.
        # -1 is required for the final element.
        rightMax = -1

        # Traverse backwards so all elements to the right
        # have already contributed to rightMax.
        for i in range(len(arr)-1,-1,-1):

            # Preserve the maximum including the current element.
            newMax = max(rightMax, arr[i])

            # Replace with the greatest element strictly to the right.
            arr[i] = rightMax

            # Carry the updated maximum into the next iteration.
            rightMax = newMax

        return arr
