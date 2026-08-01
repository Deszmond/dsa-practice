class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Problem: Return all matrix elements in clockwise spiral order.
        # Thought Process: Shrink the unvisited rectangle using four boundaries (top, bottom, left, right), traversing one edge at a time.
        # Time Complexity: O(m * n) - every cell is visited exactly once.
        # Space Complexity: O(1) extra space (excluding the output list).

        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        # Continue while there is still an unvisited rectangle.
        while left < right and top < bottom:

            # Traverse the top row (left → right).
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Traverse the right column (top → bottom).
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # Stop if no unvisited rectangle remains.
            if not (left < right and top < bottom):
                break

            # Traverse the bottom row (right → left).
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # Traverse the left column (bottom → top).
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res