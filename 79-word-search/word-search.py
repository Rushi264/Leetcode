class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Total rows and columns in the board
        ROWS, COLS = len(board), len(board[0])

        # DFS function: tries to match word[i] starting from position (r, c)
        def dfs(r, c, i):
            # If we matched all characters in word, return True
            if i == len(word):
                return True

            # Boundary checks:
            # r or c out of bounds, mismatch character, or cell already visited
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            # Mark the current cell as visited using a special placeholder
            temp = board[r][c]
            board[r][c] = '#'

            # Explore all 4 directions: down, up, right, left
            res = (
                dfs(r + 1, c, i + 1) or  # down
                dfs(r - 1, c, i + 1) or  # up
                dfs(r, c + 1, i + 1) or  # right
                dfs(r, c - 1, i + 1)     # left
            )

            # Restore the original character (backtracking)
            board[r][c] = temp
            return res

        # Try starting the DFS from every cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                # If dfs returns True from any starting cell, the word exists
                if dfs(r, c, 0):
                    return True

        # No valid path found for the word
        return False
