class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = { }
        
        for index in range( len( nums) ):
            if target - nums[ index ] in hash_map:
                return [ hash_map[ target - nums[ index ] ], index ]
            else:
                hash_map[ nums[ index ] ] = index
                
        return [ ]
