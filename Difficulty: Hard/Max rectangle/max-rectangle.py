class Solution:
    def maxArea(self, mat):
        if not mat:
            return 0

        n, m = len(mat), len(mat[0])
        heights = [0] * m
        max_area = 0

        for i in range(n):
            for j in range(m):
                # Build histogram height for each column
                heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0

            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)  # sentinel to clear stack at the end

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()  # restore original array
        return max_area