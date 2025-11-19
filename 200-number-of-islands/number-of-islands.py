from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # If the grid is empty, there are no islands.
        if not grid:
            return 0
        
        islands = 0                  # Count of islands
        visited = set()              # Keeps track of visited land cells

        def bfs(r, c):
            """
            BFS to traverse all connected land ('1') starting from (r, c).
            Marks every connected land cell as visited.
            """
            q = deque()
            q.append((r, c))         # Start BFS with the current cell
            visited.add((r, c))      # Mark the start cell as visited

            while q:
                row, col = q.popleft()   # Process one cell at a time

                # Directions to move: down, up, right, left
                directions = [(1,0), (-1,0), (0,1), (0,-1)]

                # Check all 4 neighbors
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc  # New row & column

                    # Validate boundaries and check if it's land and unvisited
                    if (0 <= nr < len(grid) and
                        0 <= nc < len(grid[0]) and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visited):

                        visited.add((nr, nc))    # Mark as visited
                        q.append((nr, nc))       # Add to queue to continue BFS

        # Traverse entire grid
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                
                # Found a new island start point (land that hasn't been visited yet)
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)       # Explore the full island
                    islands += 1    # Increase island count
        
        return islands              # Total islands found
