class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW,COL=len(matrix),len(matrix[0])
        l,r=0,COL*ROW-1

        while (l<=r):
            mid=(l+r)//2
            rowS,colS=mid//COL,mid%COL
            if matrix[rowS][colS]==target:
                return True
            if matrix[rowS][colS]<target:
                l=mid+1
            else:
                r=mid-1
        return False
