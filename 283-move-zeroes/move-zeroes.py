class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=0 # track and count no of non zero elements
        for i in range(len(nums)):
            if(nums[i] !=0):
                nums[c] = nums[i]
                c += 1
        
        for j in range(c, len(nums)):
            nums[j] = 0
      
      # Time complexity O(n)
      # space complexity O(1)


            
            
                    