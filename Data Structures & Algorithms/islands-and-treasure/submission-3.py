class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid), len(grid[0])
        v = set()
        q = deque()
        d = [[0,1],[1,0],[0,-1],[-1,0]]
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j]==0:
                    q.append((i,j))
                    v.add((i,j))
        t = 0
        while q:
            t+=1
            for _ in range(0,len(q)):
                i,j = q.popleft()
                for di,dj in d:
                    x,y = di+i,dj+j
                    if x<0 or y<0 or x>=m or y>=n or grid[x][y]==-1 or (x,y) in v:
                        continue
                    grid[x][y] = t
                    q.append((x,y))
                    v.add((x,y))
        return 
        