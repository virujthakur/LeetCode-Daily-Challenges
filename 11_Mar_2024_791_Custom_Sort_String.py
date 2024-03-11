# TC: O(26 * 26) + O(N)
# SC: O(26 * 26) + O(26)
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        graph = [[] for _ in range(26)]
        q= deque()
        indegree= [0]* 26
        m= len(order)
        for i in range(m):
            for j in range(i+1,m):
                graph[ord(order[i])-ord('a')].append(ord(order[j])-ord('a'))
                indegree[ord(order[j])-ord('a')]+=1
        
        #print(indegree)
        
        
        ans= ''
        f= defaultdict(int)
        for c in s:
            f[c]+=1
        
        for k,v in f.items():
            if not indegree[ord(k)- ord('a')]:
                q.append(k)
          
        #print(q)
        while q:
            x= q.popleft()
            #print(x)
            ans+= x* f[x]
            for y in graph[ord(x)-ord('a')]:
                indegree[y]-=1
                if not indegree[y]:
                    q.append(chr(ord('a')+y))
                    
        return ans
