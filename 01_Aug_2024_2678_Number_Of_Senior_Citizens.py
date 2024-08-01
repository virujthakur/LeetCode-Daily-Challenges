class Solution:
    #TC: O(N) SC: O(N)
    def countSeniors(self, details: List[str]) -> int:
        return len([passenger for passenger in details if int(passenger[11]+ passenger[12]) > 60])
