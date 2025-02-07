class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
       people.sort()
       boats = 0
       first ,last = 0,len(people)-1
       while(first <= last):
            if(people[first] + people[last] <= limit):
                first = first + 1
          
            boats += 1
            last  -= 1
       return boats

#Time Complexity: O(n log n)
#Space Complexity: O(1)



