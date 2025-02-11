class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        visitedNums = {}
        for num in nums:
            if num in visitedNums:
                visitedNums[num] +=1
            else:
                visitedNums[num] = 1
        
        for key, value in visitedNums.items():
            if value >= len(nums)/2:
                return key
        return -1

#Time and space complexity = O(n), O(n)
            
        