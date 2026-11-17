from typing import List


class Solution:
    # Problem: Longest Consecutive Sequence
    #
    # Thought Process:
    # Store all numbers in a set for fast membership checks.
    # Only begin counting when a number has no predecessor
    # (num - 1 is absent), meaning it starts a sequence.
    #
    # Extend forward until the next consecutive number is missing.
    # Track the longest sequence encountered.
    #
    # Pattern: Hash Set + Sequence Start Detection
    #
    # Time Complexity: O(n) expected
    # Each unique number is processed as a potential starting point.
    # Across all sequences, each number is counted at most once.
    #
    # Space Complexity: O(n)
    # The set stores up to n unique integers.

    def longestConsecutive(self, nums: List[int]) -> int:

        # Remove duplicates and enable expected O(1) membership checks.
        container = set(nums)
        longest = 0

        for num in container:

            # Only start counting if this number has no predecessor.
            # This prevents recounting the same sequence repeatedly.
            if num - 1 not in container:
                length = 1

                # Extend the sequence until the next number is missing.
                while num + length in container:
                    length += 1

                # Keep the maximum sequence length found.
                longest = max(longest, length)

        return longest