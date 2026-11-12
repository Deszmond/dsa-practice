from typing import List


class Solution:
    # Problem: Find the missing number from the range [0, n].
    #
    # Thought Process:
    # Calculate the expected sum of all numbers from 0 to n.
    # Subtract the actual sum of the numbers provided.
    # The difference must be the missing number.
    #
    # Pattern: Mathematical Difference / Running Sum
    #
    # Time Complexity: O(n)
    # Visit each number once.
    #
    # Space Complexity: O(1)
    # Only two integer variables are maintained.

    def missingNumber(self, nums: List[int]) -> int:

        # Start with n because enumerate() only generates
        # indices 0 to n-1, but the expected range includes n.
        expected_sum = len(nums)
        actual_sum = 0

        for i, num in enumerate(nums):
            expected_sum += i
            actual_sum += num

        # All present numbers cancel through subtraction,
        # leaving only the missing number.
        return expected_sum - actual_sum