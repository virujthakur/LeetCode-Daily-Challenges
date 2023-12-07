class Solution:
    # TC: O(N) SC: O(1)
    def largestOddNumber(self, num: str) -> str:
        n= len(num)
        idx = -1
        for i in range (n-1, -1, -1):
            if int(num[i]) % 2 ==1 :
                idx=i
                break;
        
        if idx == -1:  return ""
        return num[ : idx+1]
            
