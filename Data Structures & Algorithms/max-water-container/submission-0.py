class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h=heights
        a=0
        l,r=0,len(h)-1
        while (l<r):
            a=max(a,min(h[l],h[r])*(abs(l-r)))
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return a