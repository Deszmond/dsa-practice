from typing import List

def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    # Problem: How Many Numbers Are Smaller Than the Current Number
    #
    # Thought Process:
    # Sort the array to determine the relative ordering of numbers.
    # In a sorted array, the first index of a number represents
    # how many numbers are strictly smaller than it.
    #
    # Example:
    # nums = [8, 1, 2, 2, 3]
    # sorted_nums = [1, 2, 2, 3, 8]
    #
    # First occurrence indices:
    # 1 -> 0
    # 2 -> 1
    # 3 -> 3
    # 8 -> 4
    #
    # Store each number's first index in a dictionary.
    # Then iterate through the original array and replace each
    # number with its stored index.
    #
    # Time Complexity: O(n log n)
    # - Sorting the array costs O(n log n)
    # - Building the dictionary costs O(n)
    # - Building the result costs O(n)
    #
    # Space Complexity: O(n)
    # - Dictionary stores up to n unique values
    # - Result array stores n values

    store = {}

    sorted_nums = sorted(nums)

    # Store the first occurrence index of each number
    for i, v in enumerate(sorted_nums):
        if v not in store:
            store[v] = i

    res = []

    # Lookup the count of smaller numbers for each value
    for n in nums:
        res.append(store[n])

    return res