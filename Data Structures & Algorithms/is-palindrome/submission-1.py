class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join([i.lower() for i in s if i.isalpha() or i.isdigit()])
        for i in range(0,len(s)//2):
            print(s[i],s[-1-i])
            if s[i]!=s[-1-i]:
                return False
        return True