class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def isPal(s,i,j):
            while i < j:
                if s[i] != s[j]:
                    break
                i += 1
                j -= 1
            else:
                return True
            return False
        
        p = (0,0)
        n = len(s)

        if n == 1:
            return s
        
        if isPal(s,0,n-1):
            return s
       
        for j in range(n):
            i = 0
            while i < j:
                if s[i] == s[j]: 
                    if (p[1] - p[0]) < (j-i) and isPal(s,i,j):
                        p = (i,j)
                i += 1
        
        return s[p[0]:p[1]+1]
