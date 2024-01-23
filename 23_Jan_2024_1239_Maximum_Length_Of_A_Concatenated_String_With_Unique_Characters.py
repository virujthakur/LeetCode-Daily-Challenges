class Solution:
    #TC : 2^N SC: O(1)
    def maxLength(self, arr: List[str]) -> int:
        n= len(arr)
        result = ''
        def recur(idx, vis, ans):
            nonlocal result

            if idx==n :
                if len(result) < len(ans):
                    result= ans
                return
            
            flag = False
            seen = set()
            for c in arr[idx]:
                if c in vis:
                    flag= True
                    break
                if c in seen:
                    flag= True
                    break
                seen.add(c)
            
            if not flag:
                newvis= set()
                for v in vis:
                    newvis.add(v)
                for c in arr[idx]:
                    newvis.add(c)
                
                newans= ans
                newans+= arr[idx]
                recur(idx+1,newvis, newans)
            
            recur(idx+1, vis, ans)
         
        recur(0,set(),'')
        print(result)
        return len(result)
