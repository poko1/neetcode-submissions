class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        print(adj)
        v = set()
        c = 0
        def dfs(i):
            if i in v:
                return
            v.add(i)
            for j in adj[i]:
                dfs(j)
        c = 0
        for i in range(0,n):
            if i not in v:
                c+=1
                dfs(i)
        return c