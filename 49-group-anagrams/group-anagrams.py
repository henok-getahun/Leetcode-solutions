class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        ans=[]
        for s in strs:
            curr=s
            curr=''.join(sorted(curr))
            if curr in hashMap:
                hashMap[curr].append(s)
            else:
                hashMap[curr]=[s]
        for key in hashMap:
            ans.append(hashMap[key])
        return ans
    
    #Time and Space complexity = O(n*mlog(m)),O(n) where m is the length of longest string