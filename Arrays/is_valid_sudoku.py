class Solution:
    # Problem: Determine whether a partially filled Sudoku board is valid.
    #
    # Thought Process:
    # Check each row, column and 3x3 subgrid independently.
    # Use a set to remember digits already encountered in the
    # current group. If a digit appears twice, the board is invalid.
    #
    # Pattern: Hash Set + 2D Array Traversal
    #
    # Time Complexity: O(n^2), where n is the board dimension.
    # Each cell is inspected three times: once for its row,
    # once for its column and once for its subgrid.
    #
    # Space Complexity: O(n) auxiliary space.
    # Each set stores at most n distinct digits.

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check each row

        for row in board:
            seen = set()  # Fresh set: digits only need to be unique within this row.

            for num in row:
                if num.isnumeric():
                    if num in seen:
                        return False  # Duplicate found in the current row.
                    seen.add(num)

        # Check each column ('col' is the board column, 'row' is the row index)

        for col in range(len(board)):
            seen = set()  # Reset for each new column.

            for row in range(len(board)):
                num = board[row][col]

                if num.isnumeric():
                    if num in seen:
                        return False  # Duplicate found in the current column.
                    seen.add(num)

        # Check the 3x3 subgrids

        for row_start in range(0, len(board), 3):
            for col_start in range(0, len(board), 3):

                seen = set()  # Each subgrid has its own independent set.

                # Visit all nine cells inside the current subgrid.
                for i in range(row_start, row_start + 3):
                    for j in range(col_start, col_start + 3):
                        num = board[i][j]

                        if num.isnumeric():
                            if num in seen:
                                return False  # Duplicate found in this subgrid.
                            seen.add(num)

        # No duplicates found in any row, column or subgrid.
        return True