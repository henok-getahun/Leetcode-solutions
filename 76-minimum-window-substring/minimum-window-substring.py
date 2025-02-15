class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        hashT = {}
        min_window = {}
        count = 0
        ans = [-1, -1]
        ans_len = float("infinity")
        
        for char in t:
            hashT[char] = hashT.get(char, 0) + 1
        
        start = 0
        
        for end in range(len(s)):
            char = s[end]
            min_window[char] = min_window.get(char, 0) + 1
            
            if char in hashT and min_window[char] == hashT[char]:
                count += 1
            
            while count == len(hashT): 
                if (end - start + 1) < ans_len:
                    ans_len = end - start + 1
                    ans = [start, end]
                
                min_window[s[start]] -= 1
                if s[start] in hashT and min_window[s[start]] < hashT[s[start]]:
                    count -= 1
                
                start += 1  
        start, end = ans
        return s[start:end + 1] if ans_len != float("infinity") else ""
