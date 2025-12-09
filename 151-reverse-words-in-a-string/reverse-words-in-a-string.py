class Solution:
    def reverseWords(self, s: str) -> str:
        st=s.split()
        print(st)
        l=0
        r=len(st)-1
        while(l<r):
            st[l],st[r]=st[r],st[l]
            l+=1
            r-=1
        return " ".join(st)