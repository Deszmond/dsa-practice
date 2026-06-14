class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # Problem: Missing Number
        # Thought Process:
        # Compute the expected sum of numbers from 0 to n
        # while also computing the actual sum of values in nums.
        # The difference between these sums is the missing number.
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        expected_sum = len(nums)
        actual_sum = 0

        for i, num in enumerate(nums):
            expected_sum += i
            actual_sum += num

        return expected_sum - actual_sum