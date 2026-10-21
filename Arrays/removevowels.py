class Solution:
    def removeVowels(self, s: str) -> str:

        # Pattern: filtering (left-to-right scan)
        # Process: iterate through each character and keep only non-vowels
        # Time Complexity: O(n), n = length of input string
        # Space Complexity: O(n), result list stores the remaining characters
        # Note: this removes lowercase vowels only.

        vowels = "aeiou"
        result = []

        for char in s:
            if char not in vowels:
                result.append(char)
        return "".join(result)
