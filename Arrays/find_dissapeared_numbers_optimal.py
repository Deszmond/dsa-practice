class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # Problem: Find All Numbers Disappeared in an Array
        # Thought Process:
        # The numbers are guaranteed to be in the range [1, n].
        # Use each number as an index and mark that position as negative.
        # A negative value means the corresponding number exists.
        # After marking, any position that remains positive
        # represents a missing number.
        # Time Complexity: O(n)
        # Space Complexity: O(1) extra space

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result