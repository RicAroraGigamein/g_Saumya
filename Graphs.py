# 1. Problem:
# Given a 2D grid of '1' (land) and '0' (water), count the number of islands.

# Input:

# grid = [
#  ["1","1","0","0"],
#  ["1","1","0","0"],
#  ["0","0","1","0"],
#  ["0","0","0","1"]
# ]

# Output:

# 3

def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        # Boundary + water check
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        
        # Mark visited
        grid[r][c] = '0'

        # Explore all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)

    return count


# 2. Flood Fill

# Problem:
# Given an image, replace a color with a new color starting from a given pixel.

# Input:

# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2

# Output:

# [[2,2,2],[2,2,0],[2,0,1]]

def floodFill(image, sr, sc, newColor):
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]

    # Edge case: if color is already same
    if original_color == newColor:
        return image

    def dfs(r, c):
        # Boundary + color check
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if image[r][c] != original_color:
            return

        # Fill color
        image[r][c] = newColor

        # Explore 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image