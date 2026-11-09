class Solution:
    # Problem: Return an array where each element is the product
    # of every element in nums EXCEPT the element at that index.
    # Division is not allowed.

    # Thought Process:
    # Split the product into two parts:
    # 1. Everything to the LEFT of the current index (prefix).
    # 2. Everything to the RIGHT of the current index (postfix).
    #
    # Multiply these two products to get the answer.
    #
    # Instead of creating separate prefix and postfix arrays,
    # reuse the output array and two running product variables.

    # Pattern: Prefix and Suffix Products (Two-Pass Traversal)

    # Time Complexity: O(n)
    # We traverse the array twice. Each element is processed
    # a constant number of times.

    # Space Complexity: O(1) auxiliary space.
    # We only use two additional variables (prefix and postfix).
    # The output array (res) requires O(n) space.

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Initialise the output array with 1.
        # 1 is the multiplicative identity: multiplying by it
        # does not change a product.
        res = [1] * len(nums)

        prefix = 1

        # PASS 1: LEFT TO RIGHT
        # prefix represents the product of all elements
        # BEFORE the current index (excluding nums[i]).
        for i in range(len(nums)):

            # Store the product of everything to the left.
            res[i] = prefix

            # Include the current number in the running product
            # so it becomes part of the prefix for the NEXT index.
            prefix *= nums[i]

        postfix = 1

        # PASS 2: RIGHT TO LEFT
        # postfix represents the product of all elements
        # AFTER the current index (excluding nums[i]).
        for i in range(len(nums)-1, -1, -1):

            # Combine the previously stored prefix with the
            # product of everything to the right.
            res[i] *= postfix

            # Include the current number in the running product
            # so it becomes part of the postfix for the NEXT index.
            postfix *= nums[i]

        return res