from typing import List


class Solution:
    # Problem: Find the only integer that appears once,
    # while every other integer appears exactly twice.
    #
    # Thought Process:
    # XOR cancels identical numbers because:
    #
    # a ^ a = 0
    # a ^ 0 = a
    #
    # XOR is also commutative and associative, meaning
    # the order of operations does not affect the result.
    #
    # Example:
    # [4, 1, 2, 1, 2]
    #
    # 4 ^ 1 ^ 2 ^ 1 ^ 2
    # = 4 ^ (1 ^ 1) ^ (2 ^ 2)
    # = 4 ^ 0 ^ 0
    # = 4
    #
    # Pattern: Bit Manipulation / XOR
    #
    # Time Complexity: O(n)
    # Process every element once.
    #
    # Space Complexity: O(1)
    # Only one accumulator is maintained.

    def singleNumber(self, nums: List[int]) -> int:

        # XOR with 0 leaves the first number unchanged.
        xor_result = 0

        for n in nums:
            # ^= is shorthand for xor_result = xor_result ^ n.
            # Duplicate values cancel, leaving the unique value.
            xor_result ^= n

        return xor_result