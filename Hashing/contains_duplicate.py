class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Pattern: Hashset
        # Key Idea: Create a set to store values seen
        # Time: O(n)
        # Space: O(n)
        
        seen = set()

        for n in nums:
            if n in seen:
                return True

            seen.add(n)

        return False