class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # Problem: Missing Number
        # Thought Process:
        # XOR every index and every number.
        # Since duplicate values cancel each other out,
        # only the missing number remains at the end.
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        missing_number = len(nums)

        for index, value in enumerate(nums):
            missing_number ^= index
            missing_number ^= value

        return missing_number