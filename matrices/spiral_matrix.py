from typing import List


class Solution:
    # LeetCode 54: Spiral Matrix
    #
    # Problem:
    # Return all matrix elements in clockwise spiral order.
    #
    # Thought Process:
    # Maintain four boundaries representing the unvisited
    # rectangular region of the matrix.
    #
    # Traverse its edges clockwise:
    # 1. Top row: left to right
    # 2. Right column: top to bottom
    # 3. Bottom row: right to left
    # 4. Left column: bottom to top
    #
    # After each traversal, move the corresponding boundary
    # inward to exclude the elements already visited.
    #
    # Pattern: Matrix Traversal / Four Boundaries / Simulation
    #
    # Time Complexity: O(m * n)
    # m = number of rows, n = number of columns.
    # Every matrix element is visited exactly once.
    #
    # Space Complexity: O(1) auxiliary space
    # Only four boundary variables and a loop index are used.
    # Output list: O(m * n).
    #
    # Key Insight:
    # The boundaries describe the remaining unvisited region.
    # Use exclusive right and bottom boundaries, and check
    # whether the region still exists before traversing
    # the bottom and left edges.

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []

        # Left and top are inclusive boundaries.
        # Right and bottom are exclusive boundaries.
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        # Continue while the unvisited rectangle exists.
        while left < right and top < bottom:

            # Traverse the top row from left to right.
            for i in range(left, right):
                res.append(matrix[top][i])

            # The top row has now been processed.
            top += 1

            # Traverse the rightmost column from top to bottom.
            # Start at the updated top to avoid revisiting
            # the top-right corner.
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])

            # The rightmost column has now been processed.
            right -= 1

            # A single row or column may have exhausted
            # the remaining region. Without this check,
            # the next traversals could revisit elements.
            if not (left < right and top < bottom):
                break

            # Traverse the bottom row from right to left.
            # range() excludes its stop value.
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])

            # The bottom row has now been processed.
            bottom -= 1

            # Traverse the leftmost column from bottom to top.
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])

            # The leftmost column has now been processed.
            left += 1

        return res