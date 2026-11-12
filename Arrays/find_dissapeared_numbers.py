from typing import List


# ============================================================
# LEETCODE 448: FIND ALL NUMBERS DISAPPEARED IN AN ARRAY
# APPROACH 1: HASH SET
# ============================================================

class SolutionHashSet:
    # Problem: Find all missing numbers in the range [1, n].
    #
    # Thought Process:
    # Store every number encountered in a hash set.
    # Then check every expected number from 1 to n.
    # Any number absent from the set must be missing.
    #
    # Pattern: Hash Set + Membership Checking
    #
    # Time Complexity: O(n)
    # Two separate passes, with expected O(1) set operations.
    #
    # Space Complexity: O(n) auxiliary space.
    # The hash set stores up to n distinct numbers.
    # The output list also requires up to O(n) space.

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        seen = set()
        result = []

        # Record all numbers present in the input.
        for value in nums:
            seen.add(value)

        # Every expected number not in 'seen' is missing.
        for i in range(1, len(nums) + 1):
            if i not in seen:
                result.append(i)

        return result


# ============================================================
# LEETCODE 448: FIND ALL NUMBERS DISAPPEARED IN AN ARRAY
# APPROACH 2: IN-PLACE NEGATIVE MARKING
# ============================================================

class SolutionInPlace:
    # Problem: Find all missing numbers in the range [1, n].
    #
    # Thought Process:
    # Every value is guaranteed to be between 1 and n.
    # Use each value to identify an index in the original array.
    # Mark that index negative to indicate the number exists.
    #
    # After marking, positive positions represent missing numbers.
    #
    # Pattern: In-Place Array Marking / Index Mapping
    #
    # Time Complexity: O(n)
    # Two linear passes through the array.
    #
    # Space Complexity: O(1) auxiliary space.
    # The input array itself is modified to track seen numbers.
    # The output list can still require O(n) space.

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):

            # Map a number in [1, n] to an index in [0, n-1].
            # abs() is necessary because earlier iterations may
            # have already marked nums[i] as negative.
            index = abs(nums[i]) - 1

            # Mark this number as present.
            # -abs() ensures duplicates cannot flip it positive again.
            nums[index] = -abs(nums[index])

        result = []

        for i in range(len(nums)):

            # A positive position was never marked.
            # Convert the zero-based index back to its number.
            if nums[i] > 0:
                result.append(i + 1)

        return result