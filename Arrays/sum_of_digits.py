from typing import List


class Solution:
    # LeetCode 1085: Sum of Digits in the Minimum Number
    #
    # Problem:
    # Find the smallest number in an array and calculate
    # the sum of its digits.
    # Return 1 if the sum is even, otherwise return 0.
    #
    # Thought Process:
    # Use min() to identify the smallest number.
    # Extract its digits one by one using modulo 10.
    # Remove each processed digit using integer division.
    # Finally, determine whether the digit sum is even.
    #
    # Pattern: Digit Extraction / Modulo Arithmetic
    #
    # Time Complexity: O(n + d)
    # n = number of elements in nums.
    # d = number of digits in the smallest number.
    # min() scans n elements, then the while loop processes d digits.
    #
    # Space Complexity: O(1)
    # Only two integer variables are maintained.
    #
    # Key Insight:
    # n % 10 extracts the last digit.
    # n // 10 removes the last digit.
    # Repeating both operations processes every digit.

    def sumOfDigits(self, nums: List[int]) -> int:

        # Find the smallest number in the array.
        n = min(nums)

        # Accumulate the sum of its digits.
        total = 0

        while n:
            # Extract and add the rightmost digit.
            total += n % 10

            # Remove the processed digit.
            n //= 10

        # Even sum -> 1, odd sum -> 0.
        return 1 - total % 2