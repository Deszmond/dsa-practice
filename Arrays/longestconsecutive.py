class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Problem:
        # Find the length of the longest sequence of consecutive integers
        # in an unsorted array in O(n) time.

        # Thought process:
        # Store all numbers in a set for O(1) lookups.
        # Only start counting from numbers that are the beginning of a sequence
        # (i.e., num - 1 is not in the set), then extend the sequence forward.

        container = set(nums)
        longest = 0

        for num in container:
            # Start only at the beginning of a sequence.
            if num - 1 not in container:
                length = 1

                # Count consecutive numbers.
                while num + length in container:
                    length += 1

                longest = max(longest, length)

        # Time Complexity: O(n)
        # Each number is visited at most once across all sequences.
        #
        # Space Complexity: O(n)
        # The set stores all unique numbers.

        return longest