class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Problem: Sort Colors (LeetCode 75)

        Approach: Counting Sort

        Thought Process:
        1. Count the occurrences of each colour (0, 1, 2).
        2. Overwrite nums with the correct number of 0s, 1s, and 2s
           in ascending order.
        3. Modify nums in-place without returning a new list.

        Time Complexity: O(n)
        Space Complexity: O(1) auxiliary space

        Where n = len(nums).
        The buckets list always contains exactly 3 elements.
        """

        # Count how many times each colour appears.
        # Index 0 stores the count of 0s.
        # Index 1 stores the count of 1s.
        # Index 2 stores the count of 2s.
        buckets = [0, 0, 0]

        for num in nums:
            buckets[num] += 1

        # Track the position in nums that we are overwriting.
        curr = 0

        # Visit each colour in ascending order: 0, then 1, then 2.
        for i in range(len(buckets)):

            # Write the current colour as many times as it appeared.
            for j in range(buckets[i]):
                nums[curr] = i
                curr += 1