class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        #TC: O(LOG(N)* LOG(N)) SC: O(1)
        res= []
        def recur(i, less, isStarted, prev, num, path):
            nonlocal res
            if i ==len(num) and isStarted:
                # print(path, int(path))
                if int(path) >= low:
                    res.append(int(path))
                return 
            
            if i== len(num):
                # print(path)
                return 
            
            en= 9 if less == True else int(num[i])
            
            if not isStarted :
                for j in range(en+1):
                    recur(i+1, j!= en | less, isStarted | j!=0, j, num, path+ str(j))
            else:
                j = prev+1
                if not less and j > int(num[i]):
                    return
                
                recur(i+1, j!= en | less, isStarted | j!=0, j, num, path+ str(j))
        
        recur(0, False, False, -1, str(high), '')
        # print(res)
        return res
                
