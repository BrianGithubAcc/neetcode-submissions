class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res,sol=[],[]
        nums.sort()

        k=len(nums)
        def backTrack(i,subset):
            if i==k:
                res.append(subset[:])
                return

            #Subset with num[i] 
            subset.append(nums[i])   
            backTrack(i+1,subset)
            subset.pop()

            while i+1<k and nums[i]==nums[i+1]:
                i+=1
            backTrack(i+1,subset)
        backTrack(0,[])
        return res