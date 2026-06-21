class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            l = len(st)
            s+=str(l)+"#"+st
        return s

    def decode(self, s: str) -> List[str]:

        arr = []
        n = ""
        i=0
        while i<len(s):
            if s[i]=="#":
                l = i+1+int(n)
                arr.append(s[i+1:l])
                i = i+int(n)+1
                n = ""
            else:
                n += s[i]
                i+=1
        # print(arr)
        return arr