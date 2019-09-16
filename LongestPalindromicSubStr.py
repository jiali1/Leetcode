class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_val = 0
        indices = [0,0]
        
        if len( s ) < 2: 
            return s
        
        for index in range( len( s ) - 1 ):
            self.helper( s, index, index, indices )
            self.helper( s, index, index + 1, indices )
            
        return s[indices[ 0 ] : indices[ 0 ] + indices[ 1 ] ]
    
    def helper( self, s: str, left: int, right: int, indices: List[ int ] ):
        while left >= 0 and right < len( s ) and s[ left ] == s[ right ]:
            left -= 1
            right += 1 
        
        if right - left - 1 > indices[ 1 ]:
            indices[ 1 ] = right - left - 1
            indices[ 0 ] = left + 1
