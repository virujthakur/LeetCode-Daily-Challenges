class Solution:
    #TC: O(NLOGN) SC: O(1)
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()
        ans = 0
        for st, s in zip(students, seats):
            ans+= abs(st-s)
            
        return ans
