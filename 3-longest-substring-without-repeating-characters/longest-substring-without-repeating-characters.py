class Solution:  
    def lengthOfLongestSubstring(self, s: str) -> int:  
        max_len = 0  
        left = 0  
        right = 0  
        visited = {}  
        n = len(s)  

        if n <= 1:  
            return n  

        while left < n and right < n:    
            if s[right] not in visited:    
                visited[s[right]] = right    
                right += 1  
            else:  
                left = max(left, visited[s[right]] + 1)
                visited[s[right]] = right  
                right += 1  
            max_len = max(max_len, right - left)
            
        return max_len

        # Time complexity, Space complexity = O(n),O(n)