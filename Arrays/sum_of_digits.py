class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:

        # Step 1: Find the smallest number in the list
        n = min(nums)

        # Step 2: Initialise a variable to store the sum of its digits
        total = 0

        # Step 3: Loop while n is not 0
        while n:
            # Extract the last digit using modulo (%)
            total += n % 10

            # Remove the last digit using integer division (//)
            n //= 10

        # Step 4: Return 1 if the digit sum is even, otherwise return 0
        return 1 - total % 2