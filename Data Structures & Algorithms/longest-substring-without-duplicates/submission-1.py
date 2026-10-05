class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        charSet=set()
        k=len(s)
        res=0
        for r in range(k):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res=max(res,r-l+1)
        return res
