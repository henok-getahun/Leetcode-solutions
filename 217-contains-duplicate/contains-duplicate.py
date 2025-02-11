class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visitedNums={}
        for num in nums:
            if num in visitedNums:
                return True
            else:
                visitedNums[num]=0
        return False

#Time complexity , Space complexiey = O(n), O(n)
        