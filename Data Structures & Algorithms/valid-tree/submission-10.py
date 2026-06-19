class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        v = set()
        def dfs(i,p):
            v.add(i)
            for j in adj[i]:
                if j!=p:
                    if j in v:
                        return False
                    dfs(j,i)
            return True
        if not dfs(0,-1):
            return False
        return len(v)==n
        