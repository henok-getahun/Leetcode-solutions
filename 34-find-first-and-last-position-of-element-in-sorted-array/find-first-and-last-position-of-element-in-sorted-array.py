class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       
    #    starting = -1
    #    ending = -1
    #    for i in range(len(nums)):
    #        if nums[i] == target:
    #             if starting == -1:
    #                 starting = i    
    #             ending = i
    #    return [starting, ending]
    #Time complexity, Space complesity = O(n), O(n)..... it is not optimal solution

        starting = self.getStarting(nums, target)
        ending = self.getEnding(nums, target)
        return [starting, ending]

    
    def getStarting(self,nums,target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid = (left + right)//2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target :
                    return mid
                right -= 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                 left = mid + 1
        return -1

    def getEnding(self,nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid = (left + right)//2
            if nums[mid] == target:
                if mid == len(nums)-1 or nums[mid+1]!=target:
                    return mid
                left += 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1

        return -1


                 





    
     
    





    

       
    