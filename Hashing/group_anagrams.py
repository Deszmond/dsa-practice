from typing import List


class Solution:
    # LeetCode 49: Group Anagrams
    #
    # Problem:
    # Group strings that contain exactly the same characters
    # with the same frequencies, regardless of character order.
    #
    # Thought Process:
    # Anagrams share identical character frequencies.
    # Represent each word using a 26-element frequency array.
    # Convert the array into a tuple so it can be used
    # as a dictionary key.
    #
    # Words with identical frequency tuples are grouped
    # into the same list.
    #
    # Pattern: Hash Map / Frequency Counting
    #
    # Time Complexity: O(n * m) expected
    # n = number of strings.
    # m = maximum string length.
    # Each character is processed once per word.
    # Creating the 26-element array and tuple costs O(1).
    #
    # Space Complexity: O(n * m)
    # The result stores references to the input strings.
    # The dictionary also stores up to n fixed-size tuple keys.
    # Auxiliary space excluding output: O(n).
    #
    # Key Insight:
    # Anagrams have identical frequency signatures.
    # Tuples are hashable, allowing frequency counts
    # to serve as dictionary keys.

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        # Automatically creates an empty list for unseen keys.
        res = defaultdict(list)

        for word in strs:

            # Each position represents a lowercase letter a-z.
            count = [0]*26

            for char in word:

                # Convert the character into an index from 0 to 25.
                # ord('a') -> 97, so 'a' maps to index 0.
                count[ord(char)-ord('a')] += 1

            # Lists are unhashable; tuples can be dictionary keys.
            key = tuple(count)

            # All words with the same frequency signature
            # are appended to the same group.
            # defaultdict handles missing-key initialisation.
            res[key].append(word)

        # Return the grouped lists rather than the dictionary.
        return list(res.values())