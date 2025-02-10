class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            find_no = target - nums[i]
            if find_no in hashTable:
                return [i, hashTable[find_no]]
            else:
                 hashTable[nums[i]] = i
        
# Time Complexity: O(n)
# Space Complexity: O(n)

