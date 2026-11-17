from typing import List

# LeetCode 15: 3Sum
#
# Problem:
# Find all unique triplets [a, b, c] whose sum is zero.
# Each triplet must use three distinct indices.
#
# Thought Process:
# Sort the array so we can use the Two Pointers technique.
# Fix one number (a), then search for two other numbers
# that sum to -a using left (l) and right (r) pointers.
#
# Because the array is sorted:
# - Sum < 0: Move l right to increase the sum.
# - Sum > 0: Move r left to decrease the sum.
# - Sum = 0: Record the triplet and continue searching.
#
# Skip duplicate values to avoid repeated triplets.
#
# Pattern: Sorting + Two Pointers
#
# Time Complexity: O(n²)
# - Sorting: O(n log n).
# - Outer loop: O(n) iterations.
# - Inner loop: O(n) total pointer movements per iteration.
# - Overall: O(n²), since it dominates sorting.
#
# Space Complexity:
# - O(1) auxiliary space for the two-pointer search.
# - Python's sorting may use up to O(n) temporary space.
# - O(k) output space for k returned triplets.
# - nums.sort() modifies the input array in-place.
#
# Key Insight:
# Sorting allows us to eliminate combinations intelligently
# instead of checking every possible triplet in O(n³).
# Each pointer movement discards impossible candidates.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        # Fix the first number (a) of each potential triplet.
        for i, a in enumerate(nums):
            l = i + 1
            r = len(nums) - 1

            # Skip repeated anchors.
            # The previous occurrence already explored all
            # possible pairs to its right.
            if i > 0 and a == nums[i-1]:
                continue

            # l and r must represent two distinct indices.
            while l < r:
                total = a + nums[l] + nums[r]

                if total == 0:
                    res.append([a, nums[l], nums[r]])

                    # Move past the current left value.
                    # Keeping it could produce the same triplet.
                    l += 1

                    # Skip identical left values to avoid duplicates.
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

                elif total < 0:
                    # Sum is too small.
                    # Move left pointer right to increase the sum.
                    l += 1

                    # Repeated values would produce the same sum
                    # with the current anchor and right pointer.
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

                else:
                    # Sum is too large.
                    # Move right pointer left to decrease the sum.
                    r -= 1

                    # Skip repeated right values.
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1

        return res