
from typing import List


# LeetCode 11: Container With Most Water
#
# Problem:
# Given an array of vertical line heights, find the maximum
# amount of water that any two lines can contain.
#
# Thought Process:
# Start with two pointers at opposite ends to maximise width.
# Calculate the current area using:
#
#     Area = (r - l) * min(heights[l], heights[r])
#
# The shorter line limits the water height.
#
# Since moving either pointer inward decreases the width,
# we must seek a taller limiting line to potentially
# obtain a larger area.
#
# Move the pointer at the SHORTER line because keeping
# that shorter line while reducing width cannot improve
# the area.
#
# Pattern: Two Pointers (Opposite Ends / Greedy Elimination)
#
# Time Complexity: O(n)
# Each iteration moves exactly one pointer inward.
# At most n - 1 pointer movements occur.
#
# Space Complexity: O(1)
# Only pointers and scalar variables are stored.
#
# Key Insight:
# Eliminate a candidate boundary only when you can prove
# that no narrower container using it can improve the answer.


class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        curr_max = 0

        while r > l:

            # Width = distance between the two lines.
            # Height = shorter line (the limiting boundary).
            water_h = (r - l) * min(heights[l], heights[r])

            # Preserve the best area found so far.
            curr_max = max(water_h, curr_max)

            if heights[l] < heights[r]:

                # Left is shorter.
                # Keeping left fixed and moving right inward
                # makes width smaller, while water height
                # cannot exceed heights[l].
                #
                # Therefore, discard left and seek a
                # potentially taller left boundary.
                l += 1

            else:

                # Right is shorter OR both heights are equal.
                # Keeping right fixed and moving left inward
                # cannot produce a larger area.
                #
                # When heights are equal, either pointer
                # can safely move.
                r -= 1

        return curr_max
