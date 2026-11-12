from typing import List


class Solution:
    # LeetCode 75: Sort Colors
    #
    # Problem:
    # Sort an array containing only 0, 1 and 2 in ascending
    # order without using a built-in sorting function.
    # Modify the original array in-place.
    #
    # Thought Process:
    # Since there are only three possible values,
    # count how many times each colour appears.
    #
    # Then overwrite the original array with the correct
    # number of 0s, followed by 1s, followed by 2s.
    #
    # Pattern: Counting Sort / Frequency Counting
    #
    # Time Complexity: O(n)
    # First traversal: count n elements.
    # Second traversal: overwrite n elements.
    # Total: O(2n) -> O(n).
    #
    # Space Complexity: O(1) auxiliary space
    # The buckets array always contains exactly 3 elements.
    # No additional array proportional to n is created.
    #
    # Key Insight:
    # A fixed, small range of possible values allows
    # frequency counting to replace comparison-based sorting.

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Fixed-size frequency array:
        # buckets[0] = number of 0s
        # buckets[1] = number of 1s
        # buckets[2] = number of 2s
        buckets = [0, 0, 0]

        # Count each colour using its value as the bucket index.
        for num in nums:
            buckets[num] += 1

        # Pointer to the next position to overwrite.
        curr = 0

        # Process colours in ascending order.
        for i in range(len(buckets)):

            # Write colour i exactly buckets[i] times.
            # This preserves the original frequency of each colour.
            for j in range(buckets[i]):
                nums[curr] = i
                curr += 1