class Solution:
    #TC: O(LOG(N)) SC: O(1)
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans= 0
        for i in range(32):
            if (1<<i) & left :
                rem= left % (1<<(i+1))
                diff = (1<<(i+1)) - rem
                if diff > (right- left):
                    ans |= (1<<i)
                    
        return ans
