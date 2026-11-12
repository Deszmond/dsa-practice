from typing import List


# LeetCode 1365: How Many Numbers Are Smaller Than the Current Number
#
# Problem:
# For each number, count how many elements in the array
# are strictly smaller than it.
#
# Thought Process:
# Sort the array to establish the ordering of values.
# The first occurrence index of each value tells us how
# many elements are strictly smaller than that value.
#
# Store these indices in a dictionary, then use the
# original array to construct the result in its original order.
#
# Pattern: Sorting + Hash Map / First Occurrence Mapping
#
# Time Complexity: O(n log n)
# Sorting dominates the two O(n) traversals.
#
# Space Complexity: O(n)
# The sorted copy, dictionary and result each use up to O(n) space.
#
# Key Insight:
# Record only the FIRST occurrence of each number.
# Later occurrences would incorrectly count duplicates
# as strictly smaller elements.


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:

    # Maps each unique value to its first index in sorted order.
    store = {}

    # Create a sorted copy without modifying the original input.
    sorted_nums = sorted(nums)

    for i, v in enumerate(sorted_nums):

        # Preserve the first occurrence, since duplicates
        # must not count as strictly smaller numbers.
        if v not in store:
            store[v] = i

    res = []

    # Use the original ordering to construct the answer.
    # Each lookup gives the count of strictly smaller values.
    for n in nums:
        res.append(store[n])

    return res