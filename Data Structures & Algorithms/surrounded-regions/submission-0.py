class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        c = 0
        d = [[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(i,j,ch):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!="O":
                return
            grid[i][j]=ch
            for di,dj in d:
                x,y = di+i, dj+j
                dfs(x,y,ch)


        for j in range(0,len(grid[0])):
            if grid[0][j]=="O":
                dfs(0,j,"Z")
            if grid[len(grid)-1][j]=="O":
                dfs(len(grid)-1,j,"Z")

        for i in range(0,len(grid)):
            if grid[i][0]=="O":
                dfs(i,0,"Z")
            if grid[i][len(grid[0])-1]=="O":
                dfs(i,len(grid[0])-1,"Z")

        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]=="O":
                    dfs(i,j,"X")
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]=="Z":
                    grid[i][j]="O"
    

        

        
                
        