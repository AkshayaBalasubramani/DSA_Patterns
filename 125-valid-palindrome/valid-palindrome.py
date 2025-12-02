class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l=0
        r=len(st)-1
        while l<=r:
            if st[l]!=st[r]:
                return False
            l+=1
            r-=1
        return True


#no extra space utilized
    # def isPalindrome(self, s: str) -> bool:
    #     l,r = 0 ,len(s)-1

    #     while l<r:
            
    #         while l<r and not self.alphanum(s[l]):
    #             l+=1
    #         while r>l and not self.alphanum(s[r]):
    #             r-=1

    #         if s[l].lower() != s[r].lower():
    #             return False
    #         l,r = l+1,r-1
    #     return True
            

    # def alphanum(self, c):
    #     return (ord('A') <= ord(c) <= ord('Z') or
    #             ord('a') <= ord(c) <= ord('z') or
    #             ord('0') <= ord(c) <= ord('9'))
                
        
