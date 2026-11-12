from typing import List


class Solution:

    # LeetCode 1: Two Sum
    #
    # Problem:
    # Given an array of integers and a target,
    # return the indices of two distinct elements
    # whose values add up to the target.
    #
    # Thought Process:
    # Instead of checking every possible pair,
    # calculate the complement needed for each number.
    #
    # Store previously encountered numbers as dictionary
    # keys and their indices as dictionary values.
    #
    # If the complement exists in the dictionary,
    # we have found two numbers that sum to the target.
    #
    # Pattern: Hash Map / Complement Lookup
    #
    # Time Complexity: O(n) expected
    # Each element is visited at most once.
    # Dictionary lookup and insertion are O(1) on average.
    #
    # Space Complexity: O(n)
    # The dictionary may store up to n-1 elements
    # before a valid pair is found.
    #
    # Key Insight:
    # Check for the complement BEFORE inserting
    # the current number to prevent using the
    # same array element twice.

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Maps previously seen values to their indices.
        checker = {}

        for i, num in enumerate(nums):

            # Calculate the number needed to reach target.
            diff = target - num

            # If the complement was previously encountered,
            # return both indices immediately.
            if diff in checker:
                return [checker[diff], i]

            # Store the current number for future lookups.
            checker[num] = i