class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Problem:
        # Remove all occurrences of val in-place and return the number of
        # remaining elements. The order of elements does not matter.

        # Thought process:
        # Use the end of the array as a source of replacement values.
        # If nums[i] == val, replace it with the last unchecked element and
        # shrink the valid array size. Otherwise, move to the next index.

        n = len(nums)
        i = 0

        while i < n:
            if nums[i] == val:
                # Replace with the last valid element.
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1

        # Time Complexity: O(n)
        # Each element is processed at most once.
        #
        # Space Complexity: O(1)
        # Uses constant extra space.

        return n