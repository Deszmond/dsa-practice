from typing import List


class Solution:
    # LeetCode 217: Contains Duplicate
    #
    # Problem:
    # Return True if any number appears at least twice.
    # Otherwise, return False.
    #
    # Thought Process:
    # Maintain a set of previously encountered values.
    # For each number, check whether it already exists.
    # If it does, we have found a duplicate.
    #
    # Pattern: Hash Set / Duplicate Detection
    #
    # Time Complexity: O(n) expected
    # Each element is visited at most once.
    # Set membership checks and insertions are O(1) on average.
    #
    # Space Complexity: O(n) auxiliary space
    # The set may store all n unique elements.
    #
    # Key Insight:
    # Check membership BEFORE inserting the current value.
    # Otherwise, every element would appear to be a duplicate.

    def hasDuplicate(self, nums: List[int]) -> bool:

        # Store values encountered during traversal.
        seen = set()

        for n in nums:

            # If already encountered, a duplicate exists.
            # Return immediately; no further checks are needed.
            if n in seen:
                return True

            # Record the value for future membership checks.
            seen.add(n)

        # Every element was unique.
        return False