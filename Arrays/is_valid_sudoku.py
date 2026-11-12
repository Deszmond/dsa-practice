from typing import List
import collections


# ============================================================
# LEETCODE 36: VALID SUDOKU
# APPROACH 1: THREE-PASS VALIDATION
# ============================================================

class SolutionThreePass:
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


# ============================================================
# LEETCODE 36: VALID SUDOKU
# APPROACH 2: SINGLE-PASS VALIDATION
# ============================================================

class SolutionSinglePass:
    # Problem: Determine whether a partially filled Sudoku board is valid.
    #
    # Thought Process:
    # Instead of checking rows, columns and subgrids separately,
    # validate all three constraints while visiting each cell once.
    #
    # Maintain three dictionaries of sets:
    # rows[r]    -> Digits already seen in row r.
    # cols[c]    -> Digits already seen in column c.
    # squares[(r//3, c//3)] -> Digits already seen in a 3x3 box.
    #
    # Pattern: Hash Map + Hash Set + 2D Array Traversal
    #
    # Time Complexity: O(n^2), where n is the board dimension.
    # Each cell is visited once, with expected O(1) set operations.
    #
    # Space Complexity: O(n^2) auxiliary space for a generalised board.
    # The dictionaries collectively store previously encountered digits.
    #
    # Note: For the fixed 9x9 Sudoku problem, both complexities
    # are technically O(1), since the board size is constant.

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # defaultdict(set) automatically creates an empty set
        # whenever a missing key is accessed.
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r//3, c//3)

        # Visit every cell once, checking all three constraints.
        for r in range(len(board)):
            for c in range(len(board)):

                # Empty cells do not contribute to duplicate checks.
                if board[r][c] == ".":
                    continue

                # Integer division groups every three rows and columns
                # into the same 3x3 box.
                #
                # Example:
                # (0, 0), (1, 2), (2, 1) -> box (0, 0)
                # (3, 4), (4, 5), (5, 3) -> box (1, 1)

                # If the digit already exists in ANY of its three
                # groups, the board violates Sudoku's rules.
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False

                # Record the digit in all three groups.
                # Invariant: Each set contains the digits already
                # encountered in that group, with no duplicates.
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        # Every populated cell satisfied all three constraints.
        return True