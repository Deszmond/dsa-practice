class Solution:
    # Problem: Find every possible next state by flipping
    # two consecutive '+' characters into '--'.
    #
    # Thought Process:
    # Scan every pair of adjacent characters. Whenever
    # a pair is '++', create a new string with that pair
    # replaced by '--' and add it to the result.
    #
    # Pattern: Fixed-size window (2 characters).
    #
    # Time Complexity: O(n^2), where n is the string length.
    # We scan O(n) positions, and constructing each result
    # takes O(n) time due to slicing and concatenation.
    #
    # Space Complexity: O(n^2) output space in the worst case,
    # because there can be O(n) resulting strings of length n.

    def generatePossibleNextMoves(self, currentstate: str) -> List[str]:
        res = []

        # Stop at len(currentstate) - 1 because each window
        # needs two characters, and Python excludes the
        # ending index of a range.
        for i in range(len(currentstate) - 1):

            # Python slicing excludes the ending index,
            # so i:i+2 selects exactly two characters.
            if currentstate[i:i+2] == "++":

                # Preserve the prefix before the pair,
                # replace the pair with '--', and preserve
                # the suffix after the pair.
                new_state = currentstate[:i] + "--" + currentstate[i + 2:]

                res.append(new_state)

        return res