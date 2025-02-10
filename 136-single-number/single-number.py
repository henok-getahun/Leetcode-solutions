class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       sum_1 = sum(nums)
       unique = set(nums)
       sum_2 = 2*sum(unique)       
       return sum_2 - sum_1
                

                



           
                
    
        