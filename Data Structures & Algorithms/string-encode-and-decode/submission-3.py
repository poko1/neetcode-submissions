class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res+=str(len(st))
            res+="/"
            res+=st
        return res

    def decode(self, s: str) -> List[str]:
        ans = []
        # print(s)
        i = 0
        while i<len(s):
            n = 0
            j = i
            while s[j]!="/":
                c = int(s[j])
                if n!=0:
                    n*=10
                n+=c
                j+=1
            j+=1
            ans.append(s[j:j+n])
            # print(ans)
            i = j+n
            
        return ans
            

