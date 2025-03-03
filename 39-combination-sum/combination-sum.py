from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def backtrack(start_index, current_sum):
            if current_sum == target:
                res.append(cur.copy())
                return
            elif current_sum > target:
                return
            
            for i in range(start_index, len(candidates)):
                cur.append(candidates[i])
                backtrack(i, current_sum + candidates[i]) 
                cur.pop() 

        backtrack(0, 0) 
        return res
