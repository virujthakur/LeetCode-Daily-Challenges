class Solution:
    #TC: O(N^3) SC: O(N)
    def countTriplets(self, arr: List[int]) -> int:
        n= len(arr)
        prefix = [0]* n
        xorSum = 0
        for i in range(n):
            xorSum ^=  arr[i]
            prefix[i] = xorSum
        
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j, n):
                    a= (prefix[j-1] ^ prefix[i-1]) if i-1>=0 else prefix[j-1]
                    b= (prefix[k] ^ prefix[j-1]) if j-1>=0 else prefix[k]
                    
                    if a == b:
                        # print(i,j,k, a, b)
                        ans+=1
                        
        return ans
