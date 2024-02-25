class Solution:
    #TC: O(NLOG(LOG(N))) SC: O(N)
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        isPrime = [i for i in range(10**5 + 1)] 
        n= len(nums)
        for i in range(2, int(sqrt(10**5))):
            if isPrime[i] == i:
                for j in range(int(i*i), 10** 5, i):
                    isPrime[j]= i
                    
        def factorize(n):
            pfs = set()
            while n > 1:
                pfs.add(isPrime[n])
                n//= isPrime[n]
            return pfs
        
        parent= [i for i in range(10**5+1)]
        rank= [0]* (10**5 + 1)
        
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def unionf(x, y):
            px= find(x)
            py= find(y)
            if px == py:
                return 
            
            if rank[px] < rank[py]:
                parent[px] =  py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[py]+=1
        
        if n == 1:
            return True
        for num in nums:
            if num == 1:
                return False
            pf= factorize(num)
            for p in pf:
                unionf(p, num)
                
        for i in range(n-1):
            if find(nums[i]) != find(nums[i+1]):
                return False
            
        return True
        
            
                
                
