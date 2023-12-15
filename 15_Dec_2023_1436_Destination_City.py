from collections import defaultdict
class Solution:
    # N= len(paths)
    # M= len(city where paths[i]= [city1, city2])
    # TC: O(N*M) SC: O(N+1)
    def destCity(self, paths: List[List[str]]) -> str:
        
        outdegree= defaultdict(int)
        for x,y in paths :
            outdegree[x]+=1
        
        for x,y in paths :
            if outdegree[y]== 0 :
                return y
            
        return ""
