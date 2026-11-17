from typing import List


class Solution:
    # LeetCode 167: Two Sum II - Input Array Is Sorted
    #
    # Problem:
    # Find two distinct numbers in a sorted array whose
    # sum equals the target.
    # Return their 1-based indices.
    #
    # Thought Process:
    # Since the array is sorted in ascending order,
    # initialise two pointers at opposite ends.
    #
    # Calculate their sum:
    # - Equal to target: return both indices.
    # - Greater than target: move the right pointer left
    #   to decrease the sum.
    # - Less than target: move the left pointer right
    #   to increase the sum.
    #
    # Pattern: Two Pointers / Opposite Ends / Sorted Array
    #
    # Time Complexity: O(n)
    # Each iteration moves one pointer inward.
    # At most n-1 pointer movements are required.
    #
    # Space Complexity: O(1) auxiliary space
    # Only two pointers and the current sum are stored.
    # The returned pair has constant size.
    #
    # Key Insight:
    # Sorted order tells us which pointer to move.
    # Each movement safely eliminates impossible pairs
    # without checking every combination.

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Start at the smallest and largest elements.
        l, r = 0, len(numbers) - 1

        while l < r:

            # Calculate the sum of the current pair.
            curr = numbers[l] + numbers[r]

            if curr == target:

                # Problem requires 1-based indices.
                return [l + 1, r + 1]

            elif curr > target:

                # Sum too large: decrease the larger value.
                r -= 1

            else:

                # Sum too small: increase the smaller value.
                l += 1

        # Fallback if no pair exists.
        # Unreachable under LeetCode's guarantee.
        return []