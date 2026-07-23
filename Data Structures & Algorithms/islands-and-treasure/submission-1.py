class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        v = set()
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]==0:
                    q.append((i,j))
                    # v.add((i,j))
        dist=1
        d = [[0,1],[1,0],[0,-1],[-1,0]]
        while q:
            for _ in range(0,len(q)):
                i,j = q.popleft()

                for di,dj in d:
                    x,y = i+di, j+dj
                    if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y]!=2147483647:
                        continue
                    grid[x][y] = dist
                    q.append((x,y))
                    # v.add((x,y)) 

            dist+=1
        

        