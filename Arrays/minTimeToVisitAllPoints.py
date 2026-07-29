class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # Problem:
        # Return the minimum time needed to visit all points in order.
        # A diagonal move counts as 1 second and moves both x and y by 1.

        # Thought Process:
        # For each pair of consecutive points:
        # 1. Find the horizontal distance (dx).
        # 2. Find the vertical distance (dy).
        # 3. Use diagonal moves as much as possible.
        # 4. The remaining moves are horizontal or vertical.
        # Therefore, the minimum time between two points is max(dx, dy).

        total_time = 0

        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)

            total_time += max(dx, dy)

        # Time Complexity: O(n)
        # We visit each pair of consecutive points exactly once.

        # Space Complexity: O(1)
        # Only a few variables are used regardless of input size.

        return total_time