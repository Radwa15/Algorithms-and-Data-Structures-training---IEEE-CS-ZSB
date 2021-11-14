class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}
        N = len(s)
        
        def memoize(target = s, pos = 0):
            
            if pos in memo: return memo[pos]
            
            if pos > N: return 0
            
            if pos == N:
                return 1
            
            if target[pos] == '0':
                return 0
            
            res =  memoize(target, pos+1)
            
            if int(target[pos:pos+2]) <= 26:
                res += memoize(target, pos+2)
            
            memo[pos] = res
            return memo[pos]
        
        return memoize(s, 0)
