class Solution:
    #TC: O(HIGH) SC: O(1)
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high +1):
            s = str(i)
            if len(s) %2 :
                continue
            
            left = sum([int(_) for _ in s[:len(s)//2]])
            right = sum([int(_) for _ in s[len(s)//2:]])

            ans += int(left == right)

        return ans
