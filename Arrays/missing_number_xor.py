from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Problem: Single Number
        #
        # Given a non-empty array of integers, every element
        # appears exactly twice except for one element.
        # Find and return that single element.
        #
        # Thought Process:
        # XOR has two important properties:
        #
        # 1. A number XOR itself equals 0
        #    a ^ a = 0
        #
        # 2. A number XOR 0 equals itself
        #    a ^ 0 = a
        #
        # Since every duplicate appears exactly twice,
        # the duplicates cancel each other out when XORed.
        #
        # Example:
        # [4, 1, 2, 1, 2]
        #
        # 4 ^ 1 ^ 2 ^ 1 ^ 2
        # = 4 ^ (1 ^ 1) ^ (2 ^ 2)
        # = 4 ^ 0 ^ 0
        # = 4
        #
        # The remaining value is the number that appears once.
        #
        # Time Complexity: O(n)
        # - Iterate through the array once.
        #
        # Space Complexity: O(1)
        # - Only one variable is used regardless of input size.

        xor_result = 0

        for n in nums:
            xor_result ^= n

        return xor_result