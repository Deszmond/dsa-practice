class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Pattern: Two Pointers (Opposite Ends / Sorted Array)
        # Key Idea: Exploit sorted order to shrink search space
        # Time: O(n)
        # Space: O(1)

        l, r = 0, len(numbers) - 1

        while l < r:
            curr = numbers[l] + numbers[r]

            if curr == target:
                return [l + 1, r + 1]
            elif curr > target:
                r -= 1
            else:
                l += 1

        return []  # fallback if no solution (not necessary tho!)