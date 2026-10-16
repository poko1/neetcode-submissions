class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        par = [i for i in range(0,n)]
        print(par)
        count = [1]*n

        def parent(i):
            if par[i]!=i:
                par[i] = parent(par[i])
            return par[i]

        def connect(i,j):
            pi = parent(i)
            pj = parent(j)

            if pi==pj:
                return False

            if count[pi]>=count[pj]:
                par[pj] = pi
                count[pi]+=count[pj]
            else:
                par[pi] = pj
                count[pj]+=count[pi]
            return True


        for i,j in edges:
            if not connect(i,j):
                return False
        if len(edges)==n-1:
            return True
        return False
        