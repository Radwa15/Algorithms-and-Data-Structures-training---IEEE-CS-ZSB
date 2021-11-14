class Solution:
    def reverseBits(self, n: int) -> int:      
      l = 1 << 31 
      r = 1 
      
      while l > r:
        
        l_bit = 1 if n & l else 0
        r_bit = 1 if n & r else 0
        
        if l_bit != r_bit:

          n = n ^ l ^ r

        l = l >> 1
        r = r << 1
        
      return n
