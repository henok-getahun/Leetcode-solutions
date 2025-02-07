class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start = 0
        end = len(height)-1
        while(start < end):
            length = min(height[start], height[end])
            width = end-start
            max_area = max(max_area, length*width)
            if(height[start] < height[end]):
                start = start+1
            else:
                end = end-1
        return max_area
#
#Time Complexity: O(n)
#Space Complexity: O(1)