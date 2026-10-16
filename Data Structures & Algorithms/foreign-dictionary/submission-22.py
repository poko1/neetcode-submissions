class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        degrees = defaultdict(int)
        prereq = defaultdict(list)
        q = deque()
        for word in words:
            for l in word:
                degrees[l]=0
        prereq = defaultdict(list)
        for i in range(0,len(words)):
            if i+1<len(words):
                w1 = words[i]
                w2 = words[i+1]
                if w2 in w1 and w2!=w1:
                    return ""
                x,y = 0,0
                while x<len(w1) and y<len(w2):
                    if w1[x]!=w2[y]:
                        prereq[w1[x]].append(w2[y])
                        degrees[w2[y]]+=1
                        break
                    x+=1
                    y+=1
        for l,c in degrees.items():
            if c==0:
                q.append(l)
        s = ""
        while q:
            node = q.popleft()
            s+=node
            for n in prereq[node]:
                degrees[n]-=1
                if degrees[n]==0:
                    q.append(n)
        # print(degrees)
        # print(s)
        if len(degrees)==len(s):
            return s
        return ""

        