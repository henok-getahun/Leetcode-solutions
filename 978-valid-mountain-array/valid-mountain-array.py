class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        else:
           summit=0
           pointer=0
           while(arr[pointer] < arr[pointer + 1]):
                summit = summit + 1
                pointer = pointer + 1
                if(pointer >= len(arr)-1):
                        return False
           if(summit < len(arr) - 1 and summit > 0):
                while(arr[pointer] > arr[pointer + 1]):
                    pointer = pointer + 1
                    if(pointer >= len(arr)-1):
                        return True
                return False
           return False
# Time complexity = O(n)
# Space compexity = O(1)
           

            

        