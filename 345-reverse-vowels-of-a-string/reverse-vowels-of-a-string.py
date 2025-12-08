class Solution:
    def reverseVowels(self, s: str) -> str:
        sl=list(s)
        vowels="aeiouAEIOU"
        l=0
        r=len(sl)-1
        while l<r:
            if sl[l] in vowels and sl[r] in vowels:
                sl[l],sl[r]=sl[r],sl[l]
                l+=1
                r-=1
            elif sl[l] in vowels:
                r-=1
                continue
            elif sl[r] in vowels:
                l+=1
                continue
            else:
                l+=1
                r-=1
                
        return "".join(sl)
            