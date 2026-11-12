from typing import List


class Solution:
    # LeetCode 760: Find Anagram Mappings
    #
    # Problem:
    # Given two arrays containing the same elements,
    # return an array where each index i maps to an index
    # in nums2 containing the same value as nums1[i].
    #
    # Thought Process:
    # Build a dictionary mapping each value in nums2
    # to its index.
    # Then traverse nums1 and retrieve the corresponding
    # index directly from the dictionary.
    #
    # Pattern: Hash Map / Value-to-Index Mapping
    #
    # Time Complexity: O(n) expected
    # Building the dictionary takes O(n).
    # Constructing the result takes another O(n).
    # Hash lookups are O(1) on average.
    #
    # Space Complexity: O(n)
    # Dictionary: O(n) auxiliary space in the worst case.
    # Result: O(n) output space.
    #
    # Key Insight:
    # Store values as dictionary keys and indices as values.
    # This replaces repeated linear searches with direct lookups.

    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        store = {}
        res = [0]*len(nums1)

        # Map each value in nums2 to its index.
        # Duplicate values overwrite earlier indices,
        # which is permitted by this problem.
        for i, num in enumerate(nums2):
            store[num]=i

        # Retrieve the corresponding nums2 index for
        # each value in nums1, preserving nums1's order.
        for i, num in enumerate(nums1):
            res[i] = store[num]

        return res
