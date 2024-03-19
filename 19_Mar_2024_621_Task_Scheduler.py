import heapq
class Solution:
    #TC: O(N*M) SC: O(1)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        locked = []
        isLocked= set()
        f= {}
        for t in tasks:
            if t not in f:
                f[t]=1
            else:
                f[t]+=1
        
        i= 0
        while f or locked:
            # print(locked)
            while locked and i > locked[0][0]:
                isLocked.remove(locked[0][2])
                f[locked[0][2]]= locked[0][1]
                heapq.heappop(locked)
            
            if not f:
                i+=1
                continue
                
            mx= max(f, key= f.get)
            # print(mx, i)
            if mx in isLocked:
                i+=1
                continue
            else:
                f[mx]-=1
                if f[mx]== 0:
                    del f[mx]
                
                if mx in f:
                    heapq.heappush(locked, [i+n, f[mx], mx])
                    isLocked.add(mx)
                    del f[mx]
                i+=1
                
        return i
        
