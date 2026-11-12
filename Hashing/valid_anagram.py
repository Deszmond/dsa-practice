class Solution:
    # LeetCode 242: Valid Anagram
    #
    # Problem:
    # Determine whether two strings contain exactly the
    # same characters with identical frequencies.
    #
    # Thought Process:
    # Anagrams must have the same length and character counts.
    # First, eliminate strings with different lengths.
    # Then build a frequency dictionary for each string.
    # If both dictionaries are equal, the strings are anagrams.
    #
    # Pattern: Hash Map / Character Frequency Counting
    #
    # Time Complexity: O(n) expected
    # n = length of each string after the length check.
    # Each string is traversed once.
    # Dictionary updates and comparisons take O(n) at most.
    #
    # Space Complexity: O(k)
    # k = number of distinct characters.
    # Two dictionaries store up to k character-frequency pairs.
    # Worst case: O(n) for an unrestricted alphabet.
    # With a fixed 26-letter alphabet: O(1).
    #
    # Key Insight:
    # Anagrams depend on character frequencies,
    # not the order in which characters appear.

    def isAnagram(self, s: str, t: str) -> bool:

        # Different lengths mean the strings cannot be anagrams.
        if len(s) != len(t):
            return False

        # Store the character frequencies of each string.
        store_s = {}
        store_t = {}

        for char in s:
            # get() returns 0 if the character has not appeared.
            # Otherwise, retrieve its existing frequency.
            store_s[char] = store_s.get(char, 0) + 1

        for char in t:
            store_t[char] = store_t.get(char, 0) + 1

        # Dictionary equality compares keys and their values,
        # regardless of insertion order.
        return store_s == store_t