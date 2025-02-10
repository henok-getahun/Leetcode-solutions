class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n<=1:
            return 0
        isPrime = [True]*n
        isPrime[0]=isPrime[1]=False
        
        for i in range(2,math.ceil(sqrt(n))):
            for j in range(i*i,n,i):
                    isPrime[j]=False
        
        count=0
        for i in range(n):
            if isPrime[i]:
                count +=1
        return count
    

            
            
            




        