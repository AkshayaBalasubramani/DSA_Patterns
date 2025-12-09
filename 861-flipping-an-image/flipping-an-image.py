class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        lout=[]
        for i in image:
            l=0
            r=len(i)-1
            while l<r:
                i[l],i[r]=i[r],i[l]
                l+=1
                r-=1
            print(i)
            a=[]
            for j in i:
                if j==0:
                    a.append(1)
                else:
                    a.append(0)
            print(a)
            lout.append(a)

                
        return lout
            
        