class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        directions = [[0,1], [0,-1], [1, 0], [-1, 0]]
        while fresh and q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
        return time if not fresh else -1
