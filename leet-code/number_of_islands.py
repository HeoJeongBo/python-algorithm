from typing import List
from collections import deque

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]


class Solution:
    def recursive_dfs(self, grid: List[List[str]], i: int, j: int):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = 0
        self.by_dfs(grid, i, j-1)
        self.by_dfs(grid, i+1, j)
        self.by_dfs(grid, i, j+1)
        self.by_dfs(grid, i-1, j)

    def iterative_dfs(self, grid: List[List[str]], i: int, j: int):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    stack = [(i, j)]

                    while stack:
                        ii, jj = stack.pop()
                        if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] == "1":
                            grid[ii][jj] = "0"

                            stack.extend([(ii, jj-1), (ii+1, jj),
                                         (ii, jj+1), (ii-1, jj)])

        return count

    def iterative_bfs(self, grid: List[List[str]], i: int, j: int):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    stack = deque([(i, j)])

                    while stack:
                        ii, jj = stack.popleft()
                        if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] == "1":
                            grid[ii][jj] = "0"

                            stack.extend([(ii, jj-1), (ii+1, jj),
                                         (ii, jj+1), (ii-1, jj)])

        return count

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return

        # count = self.iterative_dfs(grid, 0, 0)
        # count = self.iterative_bfs(grid, 0, 0)
        # return count

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.recursive_bfs(grid, i, j)
                    count += 1

        return count
