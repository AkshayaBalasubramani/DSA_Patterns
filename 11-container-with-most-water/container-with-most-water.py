class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_h=0
        while(l<r):
            b=r-l
            h=min(height[l],height[r])
            a=h*b
            print(a)
            if a>max_h:
                max_h=a
            if height[l]>height[r]:
                r-=1
            elif height[l]<=height[r]:
                l+=1
        return max_h
