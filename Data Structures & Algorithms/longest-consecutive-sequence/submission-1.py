class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest=0
        if nums==[]:
            return 0
        nums=set(nums)
        for i in nums:
            if (i-1) in nums:
                length=0
                while (i+length) in nums:
                    length+=1
                longest=max(longest,length)
        return longest+1
            