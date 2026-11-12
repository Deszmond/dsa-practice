class Solution:
    # LeetCode 1119: Remove Vowels from a String
    #
    # Problem:
    # Remove all lowercase vowels (a, e, i, o, u)
    # from the input string.
    #
    # Thought Process:
    # Traverse the string character by character.
    # Keep only characters that are not vowels.
    # Join the retained characters into a new string.
    #
    # Pattern: String Filtering / Linear Traversal
    #
    # Time Complexity: O(n)
    # Each character is inspected once.
    # Joining the result also takes O(n) time.
    #
    # Space Complexity: O(n)
    # The result list and final string can each contain
    # up to n characters.

    def removeVowels(self, s: str) -> str:

        # Only lowercase vowels are considered.
        vowels = "aeiou"
        result = []

        # Keep characters that are not in the vowel collection.
        for char in s:
            if char not in vowels:
                result.append(char)

        # Build the final string in one operation.
        # This avoids repeated string concatenation.
        return "".join(result)
