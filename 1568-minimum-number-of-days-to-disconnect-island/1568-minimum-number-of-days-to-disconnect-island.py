class Solution(object):
    def minDays(self, grid):
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
        def floodfill(grid, i, j, lookup):
            stk = [(i, j)]
            lookup[i][j] = 1
            while stk:
                i, j = stk.pop()
                for di, dj in DIRECTIONS:
                    ni, nj = i+di, j+dj
                    if not (0 <= ni < R and 0 <= nj < C and grid[ni][nj] and not lookup[ni][nj]):
                        continue
                    lookup[ni][nj] = 1
                    stk.append((ni, nj))
         
        def count_islands(grid):
            lookup = [[0]*C for _ in xrange(R)]
            island_cnt = 0
            for i in xrange(R):
                for j in xrange(C):
                    if grid[i][j] == 0 or lookup[i][j]:
                        continue
                    island_cnt += 1
                    floodfill(grid, i, j, lookup)
            return island_cnt

        R, C = len(grid), len(grid[0])
        if count_islands(grid) != 1:
            return 0
        for i in xrange(R):
            for j in xrange(C):
                if grid[i][j] == 0:
                    continue
                grid[i][j] = 0
                island_cnt = count_islands(grid)
                grid[i][j] = 1
                if island_cnt != 1:
                    return 1
        return 2