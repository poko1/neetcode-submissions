class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)>n-1:
            return False
        adj = defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        v = set()
        def dfs(i,p):
            if i in v:
                return False
            v.add(i)
            for j in adj[i]:
                if j==p:
                    continue
                if not dfs(j,i):
                    return False
            return True
        return dfs(0,-1) and len(v)==n
        