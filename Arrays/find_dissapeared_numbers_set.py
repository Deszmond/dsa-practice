class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # Problem: Find All Numbers Disappeared in an Array
        # Thought Process:
        # Store every number we see in a hash set.
        # Then iterate through the expected range [1, n].
        # Any number not present in the set must be missing.
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        seen = set()
        result = []

        for value in nums:
            seen.add(value)

        for i in range(1, len(nums) + 1):
            if i not in seen:
                result.append(i)

        return result