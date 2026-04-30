class Solution:
    
    # Pattern: Hash Map (Value → Index Lookup)
    # Key Idea: Store seen numbers and check complement in O(1)
    # Time: O(n)
    # Space: O(n)
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in checker:
                return [checker[diff], i]

            checker[num] = i