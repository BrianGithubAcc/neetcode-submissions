class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[""]
        if not digits:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        for i in digits:
            tmp=[]
            for c in res:
                for k in digitToChar[i]:
                    tmp.append(c+k)
            res=tmp
        return res
        