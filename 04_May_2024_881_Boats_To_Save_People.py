class Solution:
    #TC: O(N) SC: O(1)
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n= len(people)
        i,j = 0,n-1
        ans = 0
        while i <= j:
            if people[i]+ people[j] <= limit:
                i+=1
                j-=1
            else:
                j-=1
            ans+=1
            
        return ans
