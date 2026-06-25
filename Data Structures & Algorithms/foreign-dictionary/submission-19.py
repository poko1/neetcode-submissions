class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        unique = set()
        for w in words[0]:
            unique.add(w)
        if len(words)<=1:
            return "".join(unique)
        for word in words:
            for w in word:
                unique.add(w)
        degrees = defaultdict(int)
        # print(unique)
        for u in unique:
            degrees[u]=0
        l=1 
        nex = defaultdict(list)
        while l<len(words):
            prev = words[l-1]
            cur = words[l]
            i,j,f = 0,0,0
            while i<len(prev) and j<len(cur):
                if prev[i]!=cur[j]:
                    nex[prev[i]].append(cur[j])
                    f = 1
                    break
                i+=1
                j+=1
            if f==0 and len(prev)>len(cur):
                return ""
            l+=1
        for i,j in nex.items():
            for n in j:
                degrees[n]+=1
        # print(nex)
        # print(degrees)
        q = deque()
        for i,j in degrees.items():
            if j==0:
                q.append(i)
        # print(q)
        res = ""
        # print(q)
        while q:
            for _ in range(len(q)):
                a = q.popleft()
                res+=a
                if a in nex:
                    for n in nex[a]:
                        degrees[n]-=1
                        if degrees[n]==0:
                            q.append(n)
        if len(res)!=len(unique):
            return ""
        return res

        