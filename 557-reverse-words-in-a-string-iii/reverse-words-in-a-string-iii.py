class Solution:
    def reverseWords(self, s: str) -> str:
        st=[]
        for i in s:
            st.append(i)
        l=0
        r=len(st)-1
        while l<r:
            st[l],st[r]=st[r],st[l]
            l+=1
            r-=1
    
        st1=("".join(st)).split()
        l1=0
        r1=len(st1)-1
        while l1<r1:
            st1[l1],st1[r1]=st1[r1],st1[l1]
            l1+=1
            r1-=1
        return " ".join(st1)

        