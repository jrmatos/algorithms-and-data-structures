class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    counter += 1
                    self.backtracking_DFS(grid, i, j)

        return counter
    
    def backtracking_DFS(self, grid, i, j):
        # base case
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
            return

        grid[i][j] = '0'

        self.backtracking_DFS(grid, i-1, j) # left
        self.backtracking_DFS(grid, i+1, j) # right
        self.backtracking_DFS(grid, i, j-1) # up
        self.backtracking_DFS(grid, i, j+1) # down
