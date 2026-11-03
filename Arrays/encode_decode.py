# Problem: Encode a list of strings into one string and decode it back
# Thought Process:
# Each word is stored as: length + "#" + word.
# The length tells decode() exactly how many characters belong
# to the current word, so we don't rely on a delimiter that might
# also appear inside the original word.
#
# Pattern: String Encoding / Length Prefix
#
# Time Complexity: O(n), where n is the total number of characters
# across all input strings. Each character is processed a constant
# number of times.
#
# Space Complexity: O(n) for the encoded string and decoded output.

class Solution:

    def encode(self, strs: List[str]) -> str:

        # Stores all words in one continuous string
        encoded = ""

        for word in strs:
            # Format: word length + separator + actual word
            # Example: "cat" becomes "3#cat"
            encoded += str(len(word)) + "#" + word

        return encoded


    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            # Find the separator marking the end of the length prefix
            j = i

            while s[j] != "#":
                j += 1

            # Convert the characters before "#" into an integer
            # Example: "3" becomes 3
            length = int(s[i:j])

            # Extract exactly 'length' characters after the separator
            # Python slicing excludes the ending index
            res.append(s[j + 1: j + 1 + length])

            # Jump to the beginning of the next encoded word
            # This skips both the length prefix and the actual word
            i = j + 1 + length

        return res