class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashMap={}
        n=len(nums1)
        ans=0
        for i in range(n):
            for j in range(n):
                sum=nums1[i] + nums2[j]
                if sum in hashMap:
                    hashMap[sum] += 1
                else:
                    hashMap[sum] = 1
        for i in range(n):
            for j in range(n):
                sum= -1*(nums3[i] + nums4[j])
                if sum in hashMap:
                    ans += hashMap[sum]
        return ans


        #time and space complexity = O(n^2), O(n^2)
            
